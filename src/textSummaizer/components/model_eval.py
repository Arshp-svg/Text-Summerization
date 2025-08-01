from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
from datasets import load_from_disk
import evaluate
import torch
import pandas as pd
from tqdm import tqdm
from textSummaizer.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

    
    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i:i + batch_size]
            

    def calculate_metric_on_test_ds(self,dataset, metric, model, tokenizer, 
                               batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                               column_text="article", 
                               column_summary="highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):
            
            inputs = tokenizer(article_batch, max_length=1024,  truncation=True, 
                            padding="max_length", return_tensors="pt")
            
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                            attention_mask=inputs["attention_mask"].to(device), 
                            length_penalty=0.8, num_beams=8, max_length=128)
            ''' parameter for length penalty ensures that the model does not generate sequences that are too long. '''
            
            # Finally, we decode the generated texts, 
            # replace the  token, and add the decoded texts with the references to the metric.
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=True) 
                for s in summaries]      
            
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            
            
            metric.add_batch(predictions=decoded_summaries, references=target_batch)
            
        #  Finally compute and return the ROUGE scores.
        score = metric.compute()
        return score

    def eval(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load from local path correctly
        from pathlib import Path
        tokenizer_path = Path(self.config.tokenizer_path)
        model_path = Path(self.config.model_path)
        
        # Check if local paths exist, otherwise use base model
        if tokenizer_path.exists():
            tokenizer = AutoTokenizer.from_pretrained(str(tokenizer_path))
        else:
            tokenizer = AutoTokenizer.from_pretrained("t5-small")
            
        if model_path.exists():
            model_t5 = AutoModelForSeq2SeqLM.from_pretrained(str(model_path)).to(device)
        else:
            model_t5 = AutoModelForSeq2SeqLM.from_pretrained("t5-small").to(device)
       
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = evaluate.load('rouge')

        score = self.calculate_metric_on_test_ds(
            dataset_samsum_pt['test'][0:100],
            rouge_metric, 
            model_t5,
            tokenizer, 
            batch_size=2, 
            column_text='dialogue', 
            column_summary='summary'
        )

        rouge_dict = dict((rn, score[rn]) for rn in rouge_names)
        df = pd.DataFrame(rouge_dict, index=['t5-small']) 
        df.to_csv(self.config.metrics_file, index=False)

