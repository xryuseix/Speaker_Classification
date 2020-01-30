from pydub import AudioSegment

# read mp3
sound = AudioSegment.from_mp3("./sample.mp3")

# 5000ms~10000ms
sound1 = sound[5000:10000]

# last 10000ms
sound2 = sound[-10000:]

# output
sound1.export("output1.mp3", format="mp3")
sound2.export("output2.mp3", format="mp3")
