#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     12-11-2018
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
#_______________________________________________________________________________
def find_peak(array):
    length = len(array)
    cnt=[]
    flag= -1
    var=0
    for i in range(1,length):
            if array[i-1]<array[i]:
                if flag == -1:
                    flag = 1
            if array[i-1]>array[i]:
                if flag == 1:
                    flag = -1
                    cnt.append(i-1)

    if len(cnt)==1:
        imax = cnt[0]
    else:
        maxm = np.max(array)
        mid = maxm/8
        for i in range(0, len(cnt)):
            #print array[cnt[i]], mid
            if array[cnt[i]] > mid:
                #print cnt[i], mid
                imax = cnt[i]
                break
        #print imax
    return imax
#_______________________________________________________________________________
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
#-------------------------------------------------------------------------------
#taking the mean and compairng with different windows
'''mean = np.mean(np.square(sound_wave))


k = int(0.05 *length)
#-------------------------------------------------------------------------------
arr=[]
arr=[[0,0]]
for i in range(0,length/k):
    if len(sound_wave) < k*(i+1):
        break
    samp = sound_wave[k*i : k*(i+1)] #getting that window in an array
    avg = np.mean(np.square(samp))
    if avg < mean:
        arr.append([k*i,k*(i+1)])
arr.append([len(sound_wave),len(sound_wave)])
#-------------------------------------------------------------------------------
new_wave=[]
for x in range(0,len(arr)-1):
        for i in sound_wave[arr[x][1]:arr[x+1][0]]:
            new_wave.append(i)'''
#-------------------------------------------------------------------------------
new_wave = sound_wave
samp = len(new_wave)
trans = abs(np.fft.rfft(new_wave))
imax= find_peak(trans)
#trans = trans[0:((600*samp)/fs)]
#imax = np.argmax(trans)
f = imax*fs/samp
print "fs",fs, "l- ",samp
print f
