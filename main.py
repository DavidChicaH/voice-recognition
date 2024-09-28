from scripts.record_audio import record_audiofile
from scripts.process_audio import process_audiofile
from utils.save_freq import save_frequencies
from utils.graphs.freq_graph import freq_graph


audiofile, filename = record_audiofile()

txt_file_path = f"./data/txt/{filename}.txt"

frequencies, amplitudes = process_audiofile(audiofile)

save_frequencies(txt_file_path, frequencies, amplitudes)

freq_graph(txt_file_path)

