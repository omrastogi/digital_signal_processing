import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------

wavefile = wave.open("Audio_3.wav", 'r')
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
mean = 0.00001
arr = [[0,0]]
k = int(0.001*length)
j=1
for i in range(0,length/k):
    samp = sound_wave[k*i : k*(i+1)]
    avg = np.mean(np.square(samp))
    if avg < mean:
        if arr[j-1][1]==k*i:
            arr[j-1][1] = k*(i+1)

        else:
            arr.append([k*i,k*(i+1)])
            j+=1
arr.append([len(sound_wave),len(sound_wave)])


arr1=[]
for i in range(0,len(arr)-1):
    arr1.append ([arr[i][1],arr[i+1][0]])


for i in range(0,len(arr1)):
    for j in range(0,len(arr1[i])):
        arr1[i][j]=float(arr1[i][j])/44100
arr=[]
for a in arr1:
    if a[1]-a[0] > 0.02:
        arr.append(a)

silence=[]
if arr[0][0]>0.04:
    silence.append([0.0, arr[0][0]])
for i in range(1,len(arr)):
    samp = [arr[i-1][1],arr[i][0]]
    silence.append(samp)
if (float(len(sound_wave))/44100)-arr[len(arr)-1][1] > 0.01:
    silence.append([arr[len(arr)-1][1],(float(len(sound_wave))/44100)])
print arr
#print silence



'''
arr2=[]
arr=[]
c=44100
for a in arr1:
    sample_space = sound_wave[int(a[0]):int(a[1])]
    mean = np.mean(np.square(sample_space))
    mean = mean
    length = len(sample_space)
    arr = [[a[0],a[0]]]
    k = int(0.1*length)
    j=1
    for i in range(0,(length/k)):
        samp = sample_space[k*i : k*(i+1)]
        #print samp
        avg = np.mean(np.square(samp))
        #print avg
        if avg > mean:
            if arr[j-1][1]==k*i+a[0]:
                arr[j-1][1] = k*(i+1)+a[0]
                print 'hello'

            else:
                #arr.append([k*i+a[0],k*(i+1)+a[0]])
                print k*i
                j+=1
        #arr.append([len(sample_space),len(sample_space)])
        break
    #print arr
    print '______________________________________________________________________'

    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            arr[i][j]=float(arr[i][j])/44100
    #print arr
    arr2.append(arr[0])
'''
#print arr2
'''
k = int(0.05 *length)
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
'''






