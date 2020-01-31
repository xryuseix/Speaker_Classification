from pydub import AudioSegment
from tqdm import tqdm
import pathlib
import re
import os

def trim(dir, file, output_root):
    # read mp3
    sound = AudioSegment.from_mp3(file)
    # time(s)
    duration = sound.duration_seconds
    
    # if not exist file
    if not os.path.exists(output_root + dir):
        os.system('mkdir ' + output_root + dir)
    
    if not os.path.exists(output_root + dir + '/' + file):
        for i in range(0,int(duration)-1):
            trimed_sound = sound[i*1000 : (i + 1)*1000]
            # output
            trimed_sound.export(output_root + dir + '/' + str(i) + '.wav', format='wav')

def search(raw_root, output_root):
    path = pathlib.Path(raw_root)
    persons = [str(p) for p in path.iterdir()]

    for person in tqdm(persons):
        personal_name = re.sub('^.*/', '', person)
        voices = [str(p) for p in pathlib.Path(person).iterdir()]
        for voice in voices:
            trim(personal_name, voice, output_root)

raw_root = './../../../../学習データ/radio_audio/trimed/'
output_root = './voice/'

if os.path.exists('../../../../学習データ/radio_audio/trimed/.DS_Store'):
    os.system('rm ../../../../学習データ/radio_audio/trimed/.DS_Store')

search(raw_root, output_root)