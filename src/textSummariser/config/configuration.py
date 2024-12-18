'''import sys
import os

# Add src directory to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from textSummariser.constants import *
from textSummariser.utils.common import read_yaml, create_directories
from textSummariser.entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        # Load the configuration and parameters from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create necessary directories
        create_directories([self.config.artifacts_root])

        # Access the 'data_ingestion' section from the config
        data_ingestion_section = self.config.get('data_ingestion', {})

        # Create the DataIngestionConfig object with the configuration data
        self.data_ingestion_config = DataIngestionConfig(config=data_ingestion_section)

    # Method to get the DataIngestionConfig object
    def get_data_ingestion_config(self):
        return self.data_ingestion_config'''
import sys
import os

# Add src directory to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from textSummariser.constants import *
from textSummariser.utils.common import read_yaml, create_directories
from textSummariser.entity import DataIngestionConfig
from textSummariser.entity import DataValidationConfig

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        # Load the configuration and parameters from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create necessary directories
        create_directories([self.config.artifacts_root])

        # Access the 'data_ingestion' section from the config
        data_ingestion_section = self.config.get('data_ingestion', {})

        # Ensure that 'data_ingestion_section' has the expected keys and pass them to DataIngestionConfig
        self.data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion_section.get('root_dir', 'default_root_dir_path')),
            source_URL=data_ingestion_section.get('source_URL', 'default_url'),
            local_data_file=Path(data_ingestion_section.get('local_data_file', 'default_local_data_file_path')),
            unzip_dir=Path(data_ingestion_section.get('unzip_dir', 'default_unzip_dir_path'))
        )

    # Method to get the DataIngestionConfig object
    def get_data_ingestion_config(self):
        return self.data_ingestion_config
    
    
    def get_data_validation_config(self)-> DataValidationConfig:
        config= self.config.data_validation
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
        )  
        
        return data_validation_config     