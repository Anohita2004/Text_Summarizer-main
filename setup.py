from setuptools import setup, find_packages

setup(
    name="TextSummarizer",
    version="0.1.0",
    description="A text summarization project",
    author="Your Name",
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
