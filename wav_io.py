import re
import os
import rwave
import pathlib
from tqdm import tqdm


def lamb(str):
    ## ========== ファイル名でソートするラムダ式 ==============================
    num = re.sub('^.*/', '', re.sub('.wav', '', str))
    return int(num)


def paths(root, dir = True):
    ## ========== ディレクトリ，ファイルの全列挙 ==============================
    res = []
    path = pathlib.Path(root)
    for po in path.iterdir():
        if dir:
            if po.is_dir() and str(po)[-6:] != 'sample':
                res.append(str(po))
        else:
            if po.is_file():
                res.append(str(po))
    if not dir:
        res = sorted(res, key=lambda str:lamb(str))
    return res


def build_source():
    ## ========== 音源をビルド ==============================
    print('Build Audio Data')
    root = './lib/voice/'
    persons = paths(root)
    for person in persons:
        files = paths(person, False)
        for file in tqdm(files[0:50]):
            name = re.sub('^.*/', '', person)
            # if not exist file
            if not os.path.exists('./lib/re_voice/' + name):
                os.system('mkdir ./lib/re_voice/' + name)
            # 変換後のファイルPATH
            num = re.sub('^.*/', '', re.sub('.wav', '', file))
            out_filepath = './lib/re_voice/' + name + '/' + num + '.wav'
            
            # 元音源読み込み
            wav, fs = rwave.read_wave(file)
            # サンプリングレートを調整
            ds_wav, ds_fs = rwave.convert_fs(wav, fs, 1024)
            # 音源の秒数を調整
            sec_wav, sec_fs = rwave.convert_sec(wav, ds_fs, 1)
            # ビルド後の音源を書き込み
            rwave.write_wave(out_filepath, sec_wav, sec_fs)
            

build_source()