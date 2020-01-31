import rwave
import pathlib

'''
wavfile = './lib/voice/do.wav'
wav, fs = rwave.read_wave(wavfile)

print(wav)
print(fs)


to_sec = 1
# サンプリングレートを調整（8kHz）
ds_wav, ds_fs = rwave.convert_fs(wav, fs, 1024)

print(ds_wav)
print(ds_fs)

# 音源の秒数を調整
sec_wav, sec_fs = rwave.convert_sec(wav, ds_fs, 1.0)

print(sec_wav)
print(sec_fs)
'''

def dirs(root):
    res = []
    path = pathlib.Path(root)
    for po in path.iterdir():
        if po.is_dir():
            res.append(str(po))
    return res

def build_source():
    ## ========== 音源をビルド ==============================
    print('Build Audio Data')
    root = './lib/voice/'
    persons = dirs(root)
    print(persons)
    # for file in tqdm(wav_files):
    #     # 変換後のファイルPATH
    #     out_filepath = file.replace(audio_config['speaker_raw_path'], audio_config['speaker_build_path'])
    #     # 元音源読み込み
    #     wav, fs = rwave.read_wave(file)
    #     # サンプリングレートを調整（8kHz）
    #     ds_wav, ds_fs = rwave.convert_fs(wav, fs, audio_config['wave_fs'])
    #     # 音源の秒数を調整
    #     sec_wav, sec_fs = rwave.convert_sec(wav, ds_fs, audio_config['wave_sec'])
    #     # ビルド後の音源を書き込み
    #     rwave.write_wave(out_filepath, sec_wav, sec_fs)

build_source()