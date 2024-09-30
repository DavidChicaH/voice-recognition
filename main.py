from scripts.record_audio import record_audiofile
from scripts.process_audio import process_audiofile
from scripts.save_freq import save_frequencies
from scripts.freq_graph import freq_graph


audiofile, filename = record_audiofile()

txt_file_path = f"./data/txt/{filename}.txt"

frequencies, amplitudes, low_amplitudes, high_amplitudes = process_audiofile(audiofile)

save_frequencies(txt_file_path, frequencies, amplitudes)

save_frequencies(txt_file_path, frequencies, low_amplitudes)

save_frequencies(txt_file_path, frequencies, high_amplitudes)

freq_graph(frequencies, amplitudes, low_amplitudes, high_amplitudes)

