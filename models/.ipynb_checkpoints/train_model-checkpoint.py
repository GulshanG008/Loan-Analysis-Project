#src/train_model.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

from src.data_preprocessing import load_data, clean_data, get_features_and_target

def train():
    df = load_data("data/raw/loan_dataset.csv")
    df = clean_data(df)

    X, y = get_features_and_target(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    print("Model trained and saved successfully")