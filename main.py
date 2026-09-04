from networksec.components.data_ingestion import DataIngestion
from networksec.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksec.execption.execption import NetworkSecurityException
from networksec.logging.logger import logging


if __name__ =="__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Starting data ingestion process")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

    except Exception as e:
        raise NetworkSecurityException(str(e)) from e