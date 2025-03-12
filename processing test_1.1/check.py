#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     13-11-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

import scipy

wavefile = wave.open("Audio_6.wav", 'r')

length = wavefile.getnframes()

fs = wavefile.getframerate()

#Creating the wave array
sound_wave = np.zeros(length)
for i in range (0,length):
    data = wavefile.readframes(1)
    data = struct.unpack("<h", data)
    sound_wave[i] = int(data[0])

sound_wave = np.divide(sound_wave, float(2**15))
#-------------------------------------------------------------------------------
maxm = np.max(sound_wave)
array = []
print maxm
cnt =0
for i in range (0, len(sound_wave)):
    if sound_wave[i]==maxm:
        array.append(i)
        cnt = i

#-------------------------------------------------------------------------------
if len(array)<10:
    y1 = sound_wave[0:cnt]
    y2 = sound_wave[cnt+1:len(sound_wave)]
    print len (y1), len(y2)
    array=[]
    maxm = np.max(y1)
    for i in range (0, len(y1)):
        if y1[i]==maxm:
            array.append(i)
    maxm = np.max(y2)
    print maxm
    for i in range (0, len(y2)):
        if y2[i]==maxm:
            array.append(i+cnt+1)

print array
if len(array)>1:
    new_wave= sound_wave[array[0]:(array[1])]

trans = abs(np.fft.rfft(new_wave))

imax = np.argmax(trans)

f = imax*fs/(len(new_wave))

print f

plt.plot(new_wave )
plt.show()