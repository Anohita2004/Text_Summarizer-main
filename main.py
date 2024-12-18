import sys
import os

# Add the src folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from textSummariser.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummariser.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e