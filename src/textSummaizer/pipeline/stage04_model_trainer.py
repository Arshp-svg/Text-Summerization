from textSummaizer.config.configuration import ConfigurationManager
from textSummaizer.components.model_trainer import ModelTrainer
from textSummaizer.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config= ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()