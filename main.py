from scripts.record_audio import record_audiofile
from scripts.process_audio import process_audiofile
from scripts.save_freq import save_frequencies
from scripts.freq_graph import freq_graph
from scripts.clean_voice import clean_voice


audiofile, filename = record_audiofile()

cleaned_audio_file = clean_voice(audiofile, filename)

txt_file_path = f"./data/txt/{filename}.txt"

txt_cleaned_file_path = f"./data/txt/{filename}_cleaned.txt"

save_frequencies(audiofile,cleaned_audio_file, filename)

freq_graph(audiofile, cleaned_audio_file, txt_file_path, txt_cleaned_file_path)

