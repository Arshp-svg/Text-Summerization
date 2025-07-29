from textSummaizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummaizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummaizer.pipeline.stage03_data_transformation import DataTransformationPipeline
from textSummaizer.pipeline.stage04_model_trainer import ModelTrainerPipeline
from textSummaizer.logging import logger
from textSummaizer.pipeline.stage05_mode_eval import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data transformation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


#i already trained the model so i will not run this stage again
# Uncomment the following lines to run the model training stage 
# STAGE_NAME = "Model training stage"
# try:
#     logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
#     model_trainer_pipeline = ModelTrainerPipeline()
#     model_trainer_pipeline.main()
#     logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e