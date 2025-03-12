import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

import scipy



wavefile = wave.open("test.wav", 'r')

length = wavefile.getnframes()

sound_wave = np.zeros(length)

fs = wavefile.getframerate()

print length, fs

for i in range (0,length):
    data = wavefile.readframes(1)
    data = struct.unpack("<h", data)
    sound_wave[i] = int(data[0])

sound_wave = np.divide(sound_wave, float(2**15))
n = len(sound_wave)

#freq = np.fft.fftfreq(sound_wave.shape[-1])

#plt.plot(sound_wave)
#plt.show()

# Finding the silence in the audio file
mean = 0
for i in range (0,len(sound_wave)):
    mean+= (sound_wave[i]**2)
mean= mean/len(sound_wave)
print mean
print len(sound_wave)
k = int(0.05* (len(sound_wave)))
avg=0
for i in range (20):
    avg=0
    if len(sound_wave) < (k*(i+1)):
        break
    y = sound_wave[k*i : k*(i+1)]
    sum  = np.sum(np.square(y))
    avg = sum/k
    #print avg

    if avg<mean:
        for j in range (k*i, k*(i+1)):
            sound_wave = np.delete(sound_wave, i)

print sound_wave

# Fourier Transformation
a = np.fft.fft(sound_wave)

#Finding the peak
imax = np.argmax(a.real)
print imax*44100/n
#freq = np.fft.fftfreq(sound_wave.shape[-1])

plt.plot(a.real)
plt.show()


























