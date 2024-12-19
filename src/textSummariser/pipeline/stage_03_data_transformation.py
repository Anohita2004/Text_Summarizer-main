from textSummariser.config.configuration import ConfigurationManager
from textSummariser.components.data_transformation import DataTransformation
from textSummariser.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Initialize ConfigurationManager to load config.yaml
        config = ConfigurationManager()

    # Get the data ingestion config
        data_transformation_config = config.get_data_transformation_config()

    # Initialize DataIngestion with the config
        data_transformation = DataTransformation(config=data_transformation_config)

    # Download the file and extract the contents
        data_transformation.convert()