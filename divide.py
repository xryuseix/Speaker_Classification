from pydub import AudioSegment
import pathlib

def trim(dir, file):
    # read mp3
    sound = AudioSegment.from_mp3(file)
    # time(s)
    duration = sound.duration_seconds

    for i in range(0,duration-1):
        trimed_sound = sound[i*1000 : (i + 1)*1000]
        # output
        trimed_sound.export(dir[0:5] + str(i) + '.mp3', format='mp3')

raw_root = './../../../学習データ/radio_audio/trimed/'
output_root = './lib/voice/'

# search
path = pathlib.Path(raw_root)
persons = [str(p) for p in path.iterdir()]

for person in persons:
    voices = [str(p) for p in pathlib.Path(person).iterdir()]
    print(voices)