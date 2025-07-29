from textSummaizer.config.configuration import ConfigurationManager
from textSummaizer.components.model_eval import ModelEvaluation
from textSummaizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config= ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.eval()