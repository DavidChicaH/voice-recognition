import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns


def train_model():
    print("Training model")
    data = pd.read_csv('./data/csv/final_audio_features.csv')

    X = data.iloc[:, 1:]  # Features
    y = data.iloc[:, 0]  # Target / Id

    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    joblib.dump(scaler, './models/scaler.pkl')

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_normalized, y, test_size=0.2, random_state=42, stratify=y
    )
    print("Model trained")
    return X_train, X_test, Y_train, Y_test
