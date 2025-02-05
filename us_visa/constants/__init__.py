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



AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


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




#########################################################################################


"""
MODEL TRAINER RELATED CONTANT START WITH MODEL_TRAINER 

"""

MODEL_TRAINER_DIR_NAME : str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR : str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE : float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH : str = os.path.join("config","model.yaml")



#############################################################################################

"""
MODEL EVALUATION related constant 
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "usvisa-models"
MODEL_PUSHER_S3_KEY = "model-registry"


APP_HOST = "0.0.0.0"
APP_PORT = 8080




