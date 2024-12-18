from textSummariser.config.configuration import ConfigurationManager
from textSummariser.components.data_validation import DataValidation
from textSummariser.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Initialize ConfigurationManager to load config.yaml
        config = ConfigurationManager()

    # Get the data ingestion config
        data_validation_config = config.get_data_validation_config()

    # Initialize DataIngestion with the config
        data_validation = DataValidation(config=data_validation_config)

    # Download the file and extract the contents
        data_validation.validate_all_files_exist()