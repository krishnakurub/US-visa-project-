# constants folder (just like flow of path)----> config entity(take from constant and make the path to change in variables in constant folder and provide them to data ingestion component )---->data ingestion component (it will give two components 1) train.csv 2) test.csv) which is stored in artifact entity and also it is input for next component ie data validattion and goes)
import os
from us_visa.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str =datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir:str =os.path.join(ARTIFACT_DIR,TIMESTAMP)
    timestamp: str = TIMESTAMP 

### calling above data class sytx:     variable:classtype =classname

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

##inside defining data ingestion constants (look in diagram )

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    drift_report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR,
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)


