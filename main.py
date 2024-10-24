from scripts.record_audio import record_audiofile
from scripts.save_freq import save_frequencies
from scripts.freq_graph import freq_graph
from scripts.clean_voice import clean_voice
from scripts.extract_features import extract_mfccs


audiofile, filename = record_audiofile()

cleaned_audio_file = clean_voice(audiofile, filename)

txt_file_path = f"./data/txt/{filename}.txt"

txt_cleaned_file_path = f"./data/txt/{filename}_cleaned.txt"

audio_data = save_frequencies(audiofile,cleaned_audio_file, filename)

print(audio_data)

freq_graph(audiofile, cleaned_audio_file, txt_file_path, txt_cleaned_file_path)

extract_mfccs(cleaned_audio_file)

