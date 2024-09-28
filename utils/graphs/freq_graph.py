import matplotlib.pyplot as plt
import numpy as np

def freq_graph(txt_file):
    data = np.loadtxt(txt_file, delimiter=",", skiprows=1)
    frequencies = data[:, 0]
    amplitudes = data[:, 1]

    plt.plot(frequencies, amplitudes)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 500)
    plt.show()
    