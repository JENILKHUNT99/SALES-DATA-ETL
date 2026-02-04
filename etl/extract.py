from etl.logger import logger # type: ignore
import pandas as pd # type: ignore

def extract_data(file_path):
    try:
        df=pd.read_csv(file_path)
        logger.info("Data extracted successfully from %s", file_path)
        return df
    except Exception as e:
        logger.error("Error extracting data from %s: %s", file_path, str(e))
        raise