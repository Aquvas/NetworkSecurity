from networksec.execption.execption import NetworkSecurityException
from networksec.logging.logger import logging

from networksec.entity.config_entity import DataIngestionConfig
from networksec.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pymongo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_collection_as_dataframe(self):
        try:
            logging.info("Exporting collection data as dataframe")
            mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = mongo_client[self.data_ingestion_config.database_name][self.data_ingestion_config.collection_name]
            df = pd.DataFrame(list(collection.find()))
            logging.info("Dataframe created successfully")

            if '_id' in df.columns:
                df.drop('_id', axis=1, inplace=True)

            df.replace({"na": np.nan}, inplace=True)    

            return df
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            logging.info("Exporting data into feature store")
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_dir)
            os.makedirs(feature_store_dir, exist_ok=True)
            dataframe.to_csv(self.data_ingestion_config.feature_store_dir, index=False, header=True)
            logging.info("Data exported into feature store successfully")
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            logging.info("Splitting data into train and test sets")
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)
            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_file_path), exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
            logging.info("Data split into train and test sets successfully")
        except Exception as e:
            raise NetworkSecurityException(e, sys)    
            

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)

            dataingestionartifact=DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )

            return dataingestionartifact
        
        except Exception as e:
            raise NetworkSecurityException(str(e)) from e


        
