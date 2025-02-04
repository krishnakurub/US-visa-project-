##### look diagram in flowchart folder
### constant folder is used tommorow if u want to do project on anoteher data base no 
#need to hardcode entire thing just change name of data base in in this folder sillilarly other variables

#### some common constants below updated later update data ingestion constants
import os
from datetime import date

DATABASE_NAME =  "US_VISA"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = "MONGODB_URL" 

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR:  str = "artifact"
FILE_NAME : str ="usvisa.csv"

MODEL_FILE_NAME = "model.pkl"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME:  str = "test.csv"


### datadrift and data validation

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

#######################

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME 

"""

DATA_INGESTION_COLLECTION_NAME: str ="visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion" ### inside artifact folder it will create this directory and inside this directory feature store and ingested is created(look diagram)
DATA_INGESTION_FEATURE_STORE_DIR: str ="feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

########################

"""DATA VALIDATION RELATED CONSTANT START WITH DATA VALIDATION """

DATA_VALIDATION_DIR_NAME : str = "datavalidation"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"

#######################################################################################
"""DATA TRANSFORMATION RELATED CONSTANT STARTED WITH  DATA_TRANSFORMATION VAR NAME"""
DATA_TRANSFORMATION_DIR_NAME: str ="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str ="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str ="transformed_object"
