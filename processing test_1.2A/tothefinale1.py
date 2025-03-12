#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     26-11-2018
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
    imax =0
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
    return imax

wavefile = wave.open("Audio_1.wav", 'r')

length = wavefile.getnframes()

fs = wavefile.getframerate()

#Creating the wave array
sound_wave = np.zeros(length)
for i in range (0,length):
    data = wavefile.readframes(1)
    data = struct.unpack("<h", data)
    sound_wave[i] = int(data[0])

sound_wave = np.divide(sound_wave, float(2**15))



Note_durations=[]
thresh = 0.0005                                                           #a value to filter the sound wave
arr = [[0,0]]
k = int(0.001*length)                                                       #taking the 1/1000th of length of array
j=1
for i in range(0,length/k):
    samp = sound_wave[k*i : k*(i+1)]                                        #taking the sample space of 0.001 from the array
    avg = np.mean(np.square(samp))                                          #finding the square mean of the sample
    if avg < thresh:                                                        #comparing the mean to the thresh
        if arr[j-1][1]==k*i:
            arr[j-1][1] = k*(i+1)                                           #if two consecutive sample array are added, they have to be merged

        else:
            arr.append([k*i,k*(i+1)])                                       #appending the sample array
            j+=1
arr.append([len(sound_wave),len(sound_wave)])

arr1=[]
for i in range(0,len(arr)-1):
    arr1.append ([arr[i][1],arr[i+1][0]])

for i in range(0,len(arr1)):
    for j in range(0,len(arr1[i])):
        arr1[i][j]=float(arr1[i][j])/44100                                  #convering the frame measure to time measure

for a in arr1:
    if a[1]-a[0] > 0.02:                                                    #clearing any errors
        Note_durations.append([round(a[0],2),round(a[1],2)])                #rounding of the value to 0.01 values

print Note_durations

for a in  Note_durations:
    new_wave = sound_wave[int(a[0]*44100):int(a[1]*44100)]
    samp = len(new_wave)
    trans = abs(np.fft.rfft(new_wave))
    imax= find_peak(trans)
    #trans = trans[0:((600*samp)/fs)]
    #imax = np.argmax(trans)
    f = imax*fs/samp
    print "fs",fs, "l- ",samp
    print "f= ",f
