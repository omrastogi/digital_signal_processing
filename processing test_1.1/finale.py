import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

def note_detect(audio_file):
    wave_file=audio_file
    length = wavefile.getnframes()
    fs = wavefile.getframerate()

    #Creating the wave array
    sound_wave = np.zeros(length)
    for i in range (0,length):
        data = wavefile.readframes(1)
        data = struct.unpack("<h", data)
        sound_wave[i] = int(data[0])

    sound_wave = np.divide(sound_wave, float(2**15))

#opening the file
for i in range(1,7):
    wavefile = wave.open("Audio_"+str(i)+".wav", 'r')
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
    mean = np.mean(np.square(sound_wave))           #taking the mean of overall wave
    k = int(0.05 *length)                           #variable to create the window
    arr=[[0,0]]
    for i in range(0,length/k):
        if len(sound_wave) < k*(i+1):
            break
        samp = sound_wave[k*i : k*(i+1)]            #getting that window in an array
        window_mean = np.mean(np.square(samp))      #taking the mean of part in window
        if window_mean < mean:                      #comparing the window's mean to overall mean
            arr.append([k*i,k*(i+1)])
    arr.append([len(sound_wave),len(sound_wave)])

    '''arr contains the indices for length of silence.
    For example arr = [[0,2000],[2000,3500],[43874,44100]]
    the usefull wave is between 3500 and 43874.
    Hence new_wave = sound_wave[3500, 43874]'''

    new_wave=[]
    for x in range(0,len(arr)-1):
            for i in sound_wave[arr[x][1]:arr[x+1][0]]:
                new_wave.append(i)
    #new_wave is the new array without silence
    #-------------------------------------------------------------------------------

    samp = len(new_wave)                             #taking sample length
    transformed_wave = abs(np.fft.rfft(new_wave))    #taking the fourier transformation
    transformed_wave = transformed_wave[0:((600*samp)/fs)]      #changing the length of frequency domain
    imax = np.argmax(transformed_wave)                          #considering the index with peak

    f = imax*fs/samp                                 #calculating the frequency
    #print f

    notes =['F3','G3','A3','B3','C4','D4','E4','F4','G4','A4','B4']
    freq = [174,196,220,246,261,293,329,349,392,440,493]

    for i in range(0,11):
        if freq[i]-f==0:
            break
        if freq[i]-f>0:
            if abs(freq[i]-f)>abs(freq[i-1]-f):
                i=i-1
                break
            if abs(freq[i]-f)<abs(freq[i-1]-f):
                break
    print notes[i]






