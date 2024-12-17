import sys
import os

# Add the src folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from textSummariser.logging import logger

# Rest of your code


logger.info("Welcome to our custom logging")
