import os
import json
import sys
from dotenv import load_dotenv

import pymongo
import numpy as np
import pandas as pd

from networksec.execption.execption import NetworkSecurityException


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
             
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_db_url = os.getenv("MONGO_DB_URL")
            if not mongo_db_url:
                raise ValueError("MONGO_DB_URL is not set in the environment or .env file.")

            self.mongo_client = pymongo.MongoClient(mongo_db_url)
            database_handle = self.mongo_client[database]
            collection_handle = database_handle[collection]
            result = collection_handle.insert_many(records)
            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=="__main__":
    load_dotenv()
    FILE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Network_data",
        "Phishing_Legitimate_full.csv",
    )
    DATABASE = "NetworkSecurity"
    collection = "NetworkData"
    networkobj=NetworkDataExtract()

    records=networkobj.cv_to_json(file_path=FILE_PATH)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(f"Total {no_of_records} records inserted into the database {DATABASE} and collection {collection}.")