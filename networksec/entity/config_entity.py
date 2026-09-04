import os
import sys
from datetime import datetime

from networksec.constants import trining_pipeline

print(trining_pipeline.PIPELINE_NAME)
print(trining_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        self.pipeline_name = trining_pipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(os.getcwd(),trining_pipeline.ARTIFACT_DIR,timestamp)
        self.timestamp = timestamp
        self.artifact_name = trining_pipeline.ARTIFACT_DIR


class DataIngestionConfig:
    def __init__(self,training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir,trining_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_dir:str = os.path.join(self.data_ingestion_dir,trining_pipeline.DATA_INGESTION_FEATURE_STORE_DIR_NAME,trining_pipeline.FILE_NAME)
        self.training_file_path:str = os.path.join(self.data_ingestion_dir,trining_pipeline.DATA_INGESTION_INGESTED_DIR,trining_pipeline.TRAIN_FILE_NAME)
        self.test_file_path:str = os.path.join(self.data_ingestion_dir,trining_pipeline.DATA_INGESTION_INGESTED_DIR,trining_pipeline.TEST_FILE_NAME)

        self.train_test_split_ratio:float = trining_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str = trining_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str = trining_pipeline.DATA_INGESTION_DATABASE_NAME