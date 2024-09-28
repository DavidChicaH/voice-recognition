from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
import numpy as np

def process_audiofile(path_file):
    fs, data = read(path_file)

    data = data.flatten()

    fft_data = fft(data)
    frequencies = fftfreq(len(data), 1/fs)

    idx_positive_frequencies = (frequencies > 0) & (frequencies <= 500)
    positive_frequencies = frequencies[idx_positive_frequencies]

    positive_amplitudes = np.abs(fft_data[idx_positive_frequencies])

    print(fs)
    return positive_frequencies, positive_amplitudes

    
