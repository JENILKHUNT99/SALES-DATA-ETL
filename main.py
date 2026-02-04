import argparse
import time
from etl.logger import logger 
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import upload_to_s3, load_to_postgres
from config.config import *
from etl.validate import validate_data

parser = argparse.ArgumentParser()
parser.add_argument("--run-date",required=True,help="Run date in YYYY-MM-DD format")
args = parser.parse_args()
RUN_DATE = args.run_date
start_time=time.time()

# Extract
data=extract_data(RAW_DATA_DIR)
data=data[data['Sale_Date']==RUN_DATE]
print(f"Processing data for date: {RUN_DATE}")
#validate data
validate_data(data)

# Transform
cleaned_data=transform_data(data)

# Save the cleaned data locally
cleaned_data.to_csv(PROCESSED_DATA_DIR, index=False)

# Load
upload_to_s3(RAW_DATA_DIR, S3_BUCKET, RAW_KEY)
upload_to_s3(PROCESSED_DATA_DIR, S3_BUCKET, PROCESSED_KEY)
load_to_postgres(cleaned_data, POSTGRES_CONFIG,RUN_DATE)

logger.info("ETL Process Completed Successfully")