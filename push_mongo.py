import os,sys,json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca=certifi.where()

import pandas as pd
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient='records')
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongodb(self,records,database_name,collection_name):
        try:
            self.database_name=database_name
            self.collection_name=collection_name
            self.records=records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database_name = self.mongo_client[self.database_name]
            self.collection_name=self.database_name[self.collection_name]
            self.collection_name.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
        FILE_PATH = "Network_Data\phisingData.csv"
        DATABASE_NAME = "NetworkSecurity"
        COLLECTION_NAME = "PhishingData"
        network_data_extract = NetworkDataExtract()
        records = network_data_extract.cv_to_json_converter(FILE_PATH)
        print(records)
        inserted_count = network_data_extract.insert_data_to_mongodb(records, DATABASE_NAME, COLLECTION_NAME)
        print(inserted_count)
