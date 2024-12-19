import os
from textSummariser.logging import logger
import transformers
import datasets
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummariser.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config):
        """
        Initialize the DataTransformation class with a configuration object.

        Args:
            config (DataTransformationConfig): Configuration object with:
                - root_dir: Path to the directory to save transformed datasets.
                - data_path: Path to the input dataset.
                - tokenizer_name: Name of the tokenizer.
        """
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
    
    def convert_example_to_features(self, example_batch):
        """
        Convert a single example batch to features suitable for training.

        Args:
            example_batch (dict): A batch containing dialogue and summary.
        
        Returns:
            dict: Encoded input and target features.
        """
        input_encodings = self.tokenizer(
            example_batch['dialogue'], 
            max_length=1024, 
            truncation=True
        )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                example_batch['summary'], 
                max_length=128, 
                truncation=True
            )

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        """
        Load the dataset, process it, and save the transformed dataset.

        Raises:
            FileNotFoundError: If the dataset path does not exist.
        """
        # Validate dataset path
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Data path '{self.config.data_path}' does not exist.")
        
        # Load dataset
        dataset_samsum = load_from_disk(self.config.data_path)
        
        # Transform the dataset
        dataset_samsum_pt = dataset_samsum.map(self.convert_example_to_features, batched=True)
        
        # Ensure the root directory exists
        os.makedirs(self.config.root_dir, exist_ok=True)

        # Save the transformed dataset
        output_path = os.path.join(self.config.root_dir, "samsum_dataset")
        dataset_samsum_pt.save_to_disk(output_path)
         
         
            