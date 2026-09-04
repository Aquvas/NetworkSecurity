import os
import sys

import numpy as np
import pandas as pd

TARGET_COLUMN ="CLASS_LABEL"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "Phishing_Legitimate_full.csv"

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkSecurity"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR_NAME: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2