import boto3 # type: ignore
import psycopg2 # type: ignore

def upload_to_s3(local_file, bucket, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(local_file, bucket, s3_key)
    print(f"✅ Uploaded {s3_key} to S3")
 
def load_to_postgres(df,db_config):
    
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    INSERT_QUERY = """
        INSERT INTO sales_data VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """
        
    for _,row in df.iterrows():
        cursor.execute(INSERT_QUERY, tuple(row))
        
    conn.commit()
    cursor.close()
    conn.close()
    
    print("✅ Data loaded into PostgreSQL successfully")