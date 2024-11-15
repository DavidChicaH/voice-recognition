import joblib
import pandas as pd
import numpy as np
from scripts.extract_and_test_features import extract_features_for_prediction
from matplotlib import pyplot as plt
import seaborn as sns


def predict():
    
    features = extract_features_for_prediction('./data/cleaned/prediction_audio_test.wav')
    features_df = pd.DataFrame(features)

    
    scaler = joblib.load('./models/scaler.pkl')
    features_normalized = scaler.transform(features_df)

    
    pca = joblib.load('./models/pca_model.pkl')
    new_audio_pca = pca.transform(features_normalized)

    
    model = joblib.load('./models/svm_model.pkl')

    
    prediction = model.predict(features_normalized)
    probabilities = model.predict_proba(features_normalized)

    
    max_prob = np.max(probabilities)
    if max_prob >= 0.6:
        user_id = prediction[0]
        print(f"ID de usuario predicho: {user_id} (Confianza: {max_prob*100:.2f}%)")
    else:
        print("La voz no coincide con ninguno de los usuarios registrados.")

    data = pd.read_csv('./data/csv/final_audio_features.csv')
    X = data.iloc[:, 1:]  # Features
    y = data.iloc[:, 0]  # Target / Id

    X_normalized = scaler.transform(X)
    X_pca = pca.transform(X_normalized)


    pca_df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
    pca_df['user_id'] = y


    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(
        x='PCA1',
        y='PCA2',
        hue='user_id',
        data=pca_df,
        palette="Set1",
        s=100,
        marker='o',
        legend='full'
    )

    plt.scatter(
        new_audio_pca[0, 0],
        new_audio_pca[0, 1],
        c='black',
        s=200,
        marker='X',
        label="Nuevo Audio"
    )

    plt.title("Distribución de características de la voz (PCA 2D) con nuevo audio", fontsize=16)
    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.legend(title="Datos")
    plt.grid(True)
    plt.show()