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

    X = data.iloc[:, 1:] # Features
    y = data.iloc[:, 0] # Target / Id

    scaler = StandardScaler()

    X_normalized = scaler.fit_transform(X)

    joblib.dump(scaler, './models/scaler.pkl')
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42, stratify=y )
    
    print("Model trained")
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Crear un DataFrame para los resultados de PCA
    pca_df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
    pca_df['user_id'] = y

    # Graficar los resultados con diferentes colores para cada ID
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PCA1', y='PCA2', hue='user_id', data=pca_df, palette="Set1", s=100, marker='o')
    plt.title("Distribución de características de la voz (PCA 2D)", fontsize=16)
    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.legend(title="ID Usuario")
    plt.grid(True)
    plt.show()
    
    return X_train, X_test, Y_train, Y_test

