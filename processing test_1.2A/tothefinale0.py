import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
import scipy

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
            print array[cnt[i]], mid
            if array[cnt[i]] > mid:
                imax = cnt[i]
                break
    return imax

def note_detect(sound_wave):

	#   Instructions
	#   ------------
	#   Input   :   audio_file -- a single test audio_file as input argument
	#   Output  :   Detected_Note -- String corresponding to the Detected Note
	#   Example :   For Audio_1.wav file, Detected_Note = "A4"

    '''wavefile=audio_file
    length = wavefile.getnframes()
    fs = wavefile.getframerate()

    #Creating the wave array
    sound_wave = np.zeros(length)
    for i in range (0,length):
        data = wavefile.readframes(1)
        data = struct.unpack("<h", data)
        sound_wave[i] = int(data[0])

    new_wave = np.divide(sound_wave, float(2**15))'''
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

    '''
    arr contains the indices for length of silence.
    For example arr = [[0,2000],[2000,3500],[43874,44100]]
    the usefull wave is between 3500 and 43874.
    Hence new_wave = sound_wave[3500, 43874]

    '''
    new_wave=[]
    for x in range(0,len(arr)-1):
            for i in sound_wave[arr[x][1]:arr[x+1][0]]:
                new_wave.append(i)
    #new_wave is the new array without silence
    #-------------------------------------------------------------------------------
    samp = len(new_wave)
    trans = abs(np.fft.rfft(new_wave))
    imax= find_peak(trans)
    #trans = trans[0:((600*samp)/fs)]
    #imax = np.argmax(trans)
    f = imax*fs/samp
    print f
    notes =['F3','G3','A3','B3','C4','D4','E4','F4','G4','A4','B4','C5','D5','E5','F5','G5','A5','B5','C6','D6','E6','F6','G6','A6','B6']
    freq = [174,196,220,246,261,293,329,349,392,440,493,523,587,659,698,783,880,987,1046,1174,1318,1396,1567,1760,1975]
    '''for i in range(0,11):
        if (f<freq[i]):
            k=i
            break
    c=(freq[k]+freq[k-1])/2
    if f>c:
        Detected_Note = notes[k]
    else:
        Detected_Note = notes[k-1]
'''

def main():
    pass

if __name__ == '__main__':
    main()

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
mean = np.mean(np.square(sound_wave))
#print 'mean',mean
mean = 0.0001
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
print arr1
arr2 =arr1
for i in range(0,len(arr1)):
    for j in range(0,len(arr1[i])):
        arr1[i][j]=float(arr1[i][j])/44100
#print arr1
#________________________________________________________________
arr=[]
for a in arr1:
    if a[1]-a[0] > 0.02:
        arr.append(a)
#print arr
onset=[]
for a in arr:
    onset.append(a[0])
#print onset

for i in range(0,len(arr)):
    new_wave = sound_wave[int(arr2[i][0]*44100):int(arr2[i][1]*44100)]
    print note_detect(new_wave)