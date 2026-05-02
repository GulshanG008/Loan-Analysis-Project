#src/data_preprocessing.py

import pandas as pd

def loan_data(path):
    df=pd.read_csv(path)
    return df

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()

    df = df.fillna(df.mean(numeric_only=True))

    if df["home_owner"].dtype == "object":
        df["home_owner"] = df["home_owner"].map({"yes": 1, "no": 0})

    return df
    
def get_features_and_target(df):
    X = df[["age", "income", "credit_score", "dependents", "home_owner"]]
    y = df["loan_approved"]
    return X, y