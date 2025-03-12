#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     27-11-2018
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

wavefile = wave.open("Audio_4.wav", 'r')

length = wavefile.getnframes()

fs = wavefile.getframerate()

#Creating the wave array
sound_wave = np.zeros(length)
for i in range (0,length):
    data = wavefile.readframes(1)
    data = struct.unpack("<h", data)
    sound_wave[i] = int(data[0])
sound_wave = np.divide(sound_wave, float(2**15))

