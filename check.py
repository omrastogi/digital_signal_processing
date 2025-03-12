from python_speech_features import mfcc
from python_speech_features import logfbank
from python_speech_features import base
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import wave
import struct
import numpy as np

(rate,sig) = wav.read('Violin/sample_'+'1'+'.wav')
file_name = 'Violin/sample_'+'1'+'.wav'
audio_file = wave.open(file_name)
length = audio_file.getnframes()
fs = audio_file.getframerate()
sound_wave = np.zeros(length)
for i in range (0,length):
    data = audio_file.readframes(1)
    data = struct.unpack("<h", data)
    sound_wave[i] = int(data[0])
audio_file.rewind()

if length == len(sound_wave):
    print ("yo")
    if rate == fs:
        print ("yeah")
'''
print sig[50]
print sound_wave[50]
def featuresplot(sig,rate,typo):
    m = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)

    mlst = []
    for i in range(0, len(m)):
        l = m[0:4]
        mlst.append(m[i][2])
    m=[]
    m.append(np.mean(mlst))

    clst=[]
    for i in range(0, len(fbank_feat)):
        l = m[0:4]
        clst.append(np.mean(fbank_feat[i]))
    c=[]
    c.append(np.mean(clst))
    plt.plot(m,c, typo)
    return  m[0],c[0]
######################################################
(rate,sig) = wav.read('Violin/sample_'+'1'+'.wav')
mfc= mfcc(sig,rate)
spec_centeroid = logbank(sig,rate)
mfc_2nd_coeff = []
for i in range(0, len(mfc)):
        mfc_2nd_coeff.append(mfc[i][2])
mean_2nd_coeff_mfc = np.mean(mfc_2nd_coeff)

mean_cent = []
for i in range(0, len(spec_centeroid)):
    mean_cent.append(np.mean(spec_centeroid[i]))
overall_centroid_mean = np.mean(mean_cent)
'''