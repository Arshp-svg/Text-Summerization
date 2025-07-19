from textSummaizer.config.configuration import ConfigurationManager
from textSummaizer.components.data_ingestion import DataIngestion
from textSummaizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        comfig= ConfigurationManager()
        data_ingestion_config = comfig.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()