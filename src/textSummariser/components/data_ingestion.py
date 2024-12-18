import os
import urllib.request as request 
import zipfile
from textSummariser.logging import logger
from textSummariser.utils.common import get_size
import urllib.request
import zipfile
import logging
from pathlib import Path
from textSummariser.entity import DataIngestionConfig
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        local_data_file = self.config.local_data_file
        # Ensure the full path for data_ingestion folder exists
        directory_path = os.path.dirname(local_data_file)
        
        # Ensure the full directory path exists (both artifacts and data_ingestion)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)  # Creates parent directories if they don't exist
            logger.info(f"Created directory: {directory_path}")
        
        if not os.path.exists(local_data_file):
            logger.info(f"Downloading file from {self.config.source_URL} to {local_data_file}")
            
            try:
                filename, headers = urllib.request.urlretrieve(url=self.config.source_URL, filename=local_data_file)
                logger.info(f"Downloaded {filename} with the following headers: \n{headers}")
            except Exception as e:
                logger.error(f"Error downloading file: {e}")
        else:
            logger.info(f"{local_data_file} already exists.")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        
        # Ensure the unzip directory exists
        if not os.path.exists(unzip_path):
            os.makedirs(unzip_path)
            logger.info(f"Created directory: {unzip_path}")
        
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted files to {unzip_path}")
        except Exception as e:
            logger.error(f"Error extracting zip file: {e}")