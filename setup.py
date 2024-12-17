import setuptools
from setuptools import setup, find_packages
with open("README.md","r",encoding="utf-8")as f:
    long_description= f.read()
__version__="0.1.0"

REPO_NAME= "Text-Summarizer-Main"
AUTHOR_USER_NAME="Anohita2004"
SRC_REPO="textSummariser" 
AUTHOR_EMAIL="anohitamukherjee@gmail.com"   
setup(
    name=SRC_REPO,
    version=__version__,
    description="A text summarization project",
    author=AUTHOR_USER_NAME,
    packages=find_packages(),
    install_requires=[
        "transformers",
        "datasets",
        "pandas",
        "torch",
        "transformers[sentencepiece]",
        "datasets",
        "sacrebleu",
        "rouge_score",
        "py7zr",
        "pandas",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "torch",
        "notebook",
        "boto3",
        "mypy-boto3-s3",
        "python-box==6.0.2",
        "ensure==1.0.2",
        "fastapi==0.78.0",
        "uvicorn==0.18.3",
        "Jinja2==3.1.2"
        
    ],
)
