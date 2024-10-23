import librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def extract_mfccs(file_path, csv_file='mfcc_spectrogram.csv'):
    """
    Función que procesa un archivo de audio, calcula sus características MFCC,
    y las guarda en un archivo CSV (en modo append).
    
    Parámetros:
    - file_path: ruta del archivo de audio.
    - csv_file: archivo CSV donde se guardan los resultados (default 'mfcc_spectrogram.csv').
    """
    
    # Cargar el archivo de audio
    y, sr = librosa.load(file_path, sr=None)

    # Calcular MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=2048, hop_length=512)

    # Crear un DataFrame para almacenar el espectrograma como un array en una columna
    data = {
        'audio_file': [file_path],
        'mfcc_spectrogram': [mfccs]  # Almacenar los MFCCs completos como un array
    }

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Append al archivo CSV existente
    df.to_csv(csv_file, mode='a', header=False, index=False)

    # Visualizar los MFCCs (opcional)
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(mfccs, x_axis='time', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title('MFCCs después de preprocesamiento')
    plt.tight_layout()
    plt.show()

    # Confirmación de que se hizo el append
    print(f"Datos del archivo {file_path} añadidos al archivo {csv_file}")