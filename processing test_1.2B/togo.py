import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

def audio_file_rewind(audio_file):
    audio_file.rewind()

def extract_sound_wave(wavefile):
    length = wavefile.getnframes()
    fs = wavefile.getframerate()
    sound_wave = np.zeros(length)
    for i in range (0,length):
        data = wavefile.readframes(1)
        if len(data) < 2:
            print data
        data = struct.unpack("<h", data)
        sound_wave[i] = int(data[0])

    sound_wave = np.divide(sound_wave, float(2**15))
    return sound_wave, length, fs

def detect_note_duration(audio_file):
    sound_wave, length, fs = extract_sound_wave(audio_file)
    mean = 0.000005
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
    Note_durations=[]
    for a in arr1:
        if a[1]-a[0] > 0.02:
            Note_durations.append([round(a[0],2),round(a[1],2)])
    audio_file_rewind(audio_file)
    return Note_durations

def detect_silence_duration(audio_file):
    sound_wave, length, fs = extract_sound_wave(audio_file)
    mean = 0.000001
    arr = [[0,0]]
    k = int(0.001*length)
    j=1
    for i in range(0,length/k):
        samp = sound_wave[k*i : k*(i+1)]
        avg = np.mean(np.square(samp))
        if avg > mean:
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

    Silence_durations=[]
    for a in arr1:
        if a[1]-a[0] > 0.02:
            Silence_durations.append([round(a[0],2),round(a[1],2)])
            audio_file_rewind(audio_file)
    return Silence_durations
#-------------------------------------------------------------------------------

audio_file = wave.open("Audio_1.wav", 'r')
print "note detected\n",detect_note_duration(audio_file)
#audio_file.rewind()
print "silence detected"
print  detect_silence_duration(audio_file)

#-------------------------------------------------------------------------------
'''mean = 0.00001
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
print arr

silence=[]
if arr[0][0]>0.04:
    silence.append([0.0, arr[0][0]])
for i in range(1,len(arr)):
    samp = [arr[i-1][1],arr[i][0]]
    silence.append(samp)
if (float(len(sound_wave))/44100)-arr[len(arr)-1][1] > 0.01:
    silence.append([arr[len(arr)-1][1],(float(len(sound_wave))/44100)])
print arr
print silence
'''