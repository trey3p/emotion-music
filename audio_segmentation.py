#Seperating vocals from background music

#Getting the file names
import os
audio_files = os.listdir('/Users/treyplante3/Google Drive/CS & DS/Delta Lab/Ad Music Analysis/Audio')
audio_files = ['Audio/' + file for file in audio_files]
#audio_files.remove('Audio/Icon\r')
print(audio_files)


#Some of the .wav files are empty, meaning they have no sound. This is because some of the ads are just videos with no audio and we don't care abou these. We filter through these by checking if the .wav data has any nonzero values. If the values are nonzero, then there is sound.

import numpy as np
import librosa

audio_files_cleaned = [] 


from tqdm import tqdm

if not os.path.exists('audio_files_cleaned.txt'): 
    for file in tqdm(audio_files):
        y, sr = librosa.load(file)
        if np.any(y):
            audio_files_cleaned.append(file)

    with open("audio_files_cleaned.txt", "w") as writer:
        for i in tqdm(audio_files_cleaned):
            writer.write(i + "\n")



import spleeter
#Using 2stems model from spleeter

with open('audio_files_cleaned.txt') as file:
    for line in tqdm(file):
        
    
        filename = line.strip()
     #FIX: passing audio_files_cleaned is not working, says is not recognizng file 'audio_files_cleaned'
        os.system('spleeter separate -o output/ ' + filename)
