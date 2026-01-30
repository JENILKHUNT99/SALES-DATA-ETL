from Scripts.extract import extract_data
from Scripts.transform import transform_data
from Scripts.load import upload_to_s3, load_to_postgres
from config.config import *

# Extract
data=extract_data(RAW_DATA_DIR)

# Transform
cleaned_data=transform_data(data)

# Save the cleaned data locally
cleaned_data.to_csv(PROCESSED_DATA_DIR, index=False)

# Load
upload_to_s3(RAW_DATA_DIR, S3_BUCKET, RAW_KEY)
upload_to_s3(PROCESSED_DATA_DIR, S3_BUCKET, PROCESSED_KEY)
load_to_postgres(cleaned_data, POSTGRES_CONFIG)

print("ETL Process Completed Successfully")