import os
from textSummaizer.logging import logger
from textSummaizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from pathlib import Path



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        logger.info(f"Tokenizer loaded from {self.config.tokenizer_name}")

    
    
    def convert_example_to_features(self,example_batch):
        input_encodings = self.tokenizer(
            example_batch['dialogue'],
            truncation=True,
            padding='max_length',
            max_length=1024,
        )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                example_batch['summary'],
                truncation=True,
                padding='max_length',
                max_length=128,
            )
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
        
    def convert(self):
        # Load from the correct path (data ingestion output, not hardcoded)
        dataset_samsum = load_from_disk(self.config.data_path)  # Use config path
        
        dataset_samsum_pt = dataset_samsum.map(self.convert_example_to_features, batched=True)
        
        # Use Path for saving
        save_path = Path(self.config.root_dir) / "samsum_dataset"
        dataset_samsum_pt.save_to_disk(str(save_path))
