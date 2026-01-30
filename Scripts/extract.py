import pandas as pd # type: ignore

def extract_data(file_path):
    
    df=pd.read_csv(file_path)

    print("Data extracted successfully")

    return df