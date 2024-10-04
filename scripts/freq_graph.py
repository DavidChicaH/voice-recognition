import matplotlib.pyplot as plt
import librosa.display
import numpy as np

def freq_graph(audiofile, cleaned_audio_file, txt_file_path, txt_cleaned_file_path):
    
    original_audio, original_sr = librosa.load(audiofile)
    cleaned_audio, cleaned_sr = librosa.load(cleaned_audio_file)
    
    data = np.loadtxt(txt_file_path, delimiter=",", skiprows=1)
    cleaned_data = np.loadtxt(txt_cleaned_file_path, delimiter=",", skiprows=1)
    
    frequencies = data[:, 0]
    amplitudes = data[:, 1]
    
    clean_frequencies = cleaned_data[:, 0]
    clean_amplitudes = cleaned_data[:, 1]
    
    plt.figure(figsize=(10, 8))
    
        # Gráfico del audio crudo
    plt.subplot(2, 2, 1)
    librosa.display.waveshow(original_audio, sr=original_sr)
    plt.title('Voz Cruda')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')

# Gráfico del audio filtrado
    plt.subplot(2, 2, 2)
    librosa.display.waveshow(cleaned_audio, sr=cleaned_sr)
    plt.title('Voz Limpia')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.tight_layout()
    
    plt.subplot(2, 2, 3)
    plt.plot(frequencies, amplitudes, label="Sin filtros", color='red')
    plt.title("Sin Filtro")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.xlim(0, 100)
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(clean_frequencies, clean_amplitudes, label="Con filtros", color='blue')
    plt.title("Sin Filtro")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.xlim(0, 100)
    plt.grid(True)
    plt.show()
"""
    # Gráfico de las frecuencias sin filtrar
    plt.subplot(3, 1, 1)
    plt.plot(frequencies, amplitudes, label="Sin filtro", color='blue')
    plt.title("Sin Filtro")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.xlim(0, 100)
    plt.grid(True)

    # Gráfico de las frecuencias con filtro pasa bajas
    plt.subplot(3, 1, 2)
    plt.plot(frequencies, low_amplitudes, label="Filtro Pasa Bajas", color='green')
    plt.title("Filtro Pasa Bajas")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.xlim(0, 100)
    plt.grid(True)

    # Gráfico de las frecuencias con filtro pasa altas
    plt.subplot(3, 1, 3)
    plt.plot(frequencies, high_amplitudes, label="Filtro Pasa Altas", color='red')
    plt.title("Filtro Pasa Altas")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.xlim(250, 500)
    plt.grid(True)

    plt.tight_layout()
    plt.show()
   """ 