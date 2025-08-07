from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        # Example configuration, replace with actual config
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Starting data ingestion process")
        data_ingestion_artifact=data_ingestion.initialize_data_ingestion()
        print(f"Data Ingestion Artifact: {data_ingestion_artifact}")
        
    except NetworkSecurityException as e:
        raise NetworkSecurityException(e, sys)