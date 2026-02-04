from etl.logger import logger # type: ignore

def validate_data(df):
    if (df["Quantity_Sold"] < 0).any():
        raise ValueError("Negative quantity found")

    if (df["Unit_Price"] < 0).any():
        raise ValueError("Negative price found")

    if df.isnull().any().any():
        raise ValueError("Null values detected")

    logger.info("Data validation passed")
    return True
