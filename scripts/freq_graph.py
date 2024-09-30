import matplotlib.pyplot as plt
import numpy as np

def freq_graph(frequencies, amplitudes, low_amplitudes, high_amplitudes):
    plt.figure(figsize=(10, 8))

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
    