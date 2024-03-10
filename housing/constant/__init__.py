import os
from datetime import datetime

ROOT_DIR = os.getcwd() # Get the root directory of the project
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

CURRENT_DATE_TIME = f"{datetime.now():%Y-%m-%d-%H-%M-%S}"

# Training pipeline related constants
TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"

# Data Ingestion related constants
DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"
DATA_INGESTION_DOWNLOAD_DIR="dataset_download_dir"
DATA_INGESTION_RAW_DATA_DIR_KEY="raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY="tgz_download_dir"
DATA_INGESTION_DIR_NAME_KEY="dir_name"
DATA_INGESTION_TRAIN_DIR_KEY="train_dir"
DATA_INGESTION_TEST_DIR_KEY="test_dir"