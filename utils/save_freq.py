import numpy as np

def save_frequencies(txt_file, frequencies, amplitudes):
    data = np.column_stack((frequencies, amplitudes))
    np.savetxt(txt_file, data, delimiter=",")

    print(f"File saved as {txt_file}")
