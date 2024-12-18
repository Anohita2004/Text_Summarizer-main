from textSummariser.config.configuration import ConfigurationManager
from textSummariser.components.data_ingestion import DataIngestion
from textSummariser.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Initialize ConfigurationManager to load config.yaml
        config = ConfigurationManager()

    # Get the data ingestion config
        data_ingestion_config = config.get_data_ingestion_config()

    # Initialize DataIngestion with the config
        data_ingestion = DataIngestion(config=data_ingestion_config)

    # Download the file and extract the contents
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()