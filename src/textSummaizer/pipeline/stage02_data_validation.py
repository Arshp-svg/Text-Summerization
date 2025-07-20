from textSummaizer.config.configuration import ConfigurationManager
from textSummaizer.components.data_validation import DataValidation
from textSummaizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        status = data_validation.validate_all_files_exist()
        logger.info(f"Data validation status: {status}")