from etl.logger import logger # type: ignore
import boto3 # type: ignore
import psycopg2 # type: ignore
from psycopg2.extras import execute_batch # type: ignore

def upload_to_s3(local_file, bucket, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(local_file, bucket, s3_key)
    logger.info(f"Uploaded {s3_key} to S3")
 
def load_to_postgres(df,db_config,run_date):
    
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    delete_query = "DELETE FROM sales_data WHERE Sale_Date = %s"
    cursor.execute(delete_query, (run_date,))
    logger.info(f"Deleted existing data for {run_date}")
    
    INSERT_QUERY = """
        INSERT INTO sales_data VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """

    execute_batch(cursor, INSERT_QUERY, df.values.tolist())     
        
    conn.commit()
    cursor.close()
    conn.close()
    
    logger.info("Data loaded into PostgreSQL successfully")