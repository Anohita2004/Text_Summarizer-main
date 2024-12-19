from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list    
    
@dataclass(frozen=True)  # Immutable configuration object
class DataTransformationConfig:
    root_dir: Path        # Directory to save transformed datasets
    data_path: Path       # Path to the input dataset
    tokenizer_name: str   # Tokenizer name as a string    