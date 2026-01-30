import pandas as pd # type: ignore

def transform_data(df):
    
    # Convert Sale_Date to datetime
    df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
    
    #Create new calculated columns
    df["Revenue"] = df["Quantity_Sold"] * df["Unit_Price"]
    df["Revenue"] = df["Revenue"].round(2)
    df["Cost"] = df["Quantity_Sold"] * df["Unit_Cost"]
    df["Cost"] = df["Cost"].round(2)
    df["Profit"] = df["Revenue"] - df["Cost"]
    df["Profit"] = df["Profit"].round(2)
    
    print("Data transformed successfully")
    return df