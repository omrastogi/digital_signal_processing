from python_speech_features import mfcc
from python_speech_features import logfbank
from python_speech_features import base
from python_speech_features import ssc
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
import wave
import struct
#from sklearn import train_test_split
import pickle

def featuresplot(sig,rate,typo):
    m = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)
    s= ssc(sig,rate)
    mlst = []
    klst = []
    slst = []
    for i in range(0, len(m)):
        l = m[0:4]
        mlst.append(m[i][2])
        klst.append(m[i][1])
        slst.append(s[i][4])
    m=[]
    k=[]
    s=[]
    m.append(np.mean(mlst))
    k.append(np.mean(klst))
    s.append(np.mean(slst))
    clst=[]
    for i in range(0, len(fbank_feat)):
        l = m[0:4]
        clst.append(np.mean(fbank_feat[i]))
    c=[]
    c.append(np.mean(clst))
    plt.plot(m,c, typo)
    return  s[0],m[0],c[0],k[0]

def get_audio(file):
    audio_file = wave.open(file)
    length = audio_file.getnframes()
    signal = np.zeros(length)
    for i in range (0,length):
        data = audio_file.readframes(1)
        data = struct.unpack("<h", data)
        signal[i] = int(data[0])
    rate = audio_file.getframerate()
    signal = np.divide(signal, float(2**15))
    return signal, rate



dataset= []
print ("Extracting Dataset")
print ("\nviolin:"),
for i in range(1,40):
    print (i),
    file ='Violin/sample_'+str(i)+'.wav'
    sig, rate = get_audio(file)
    typo = '.y'
    s,m,c,k = featuresplot(sig, rate, typo)
    dataset.append(['violin',s,m,c,k])

print ("\ntrumpet:"),
for i in range(1,53):
    print (i),
    file = 'Trumpet/sample_'+str(i)+'.wav'
    sig, rate = get_audio(file)
    typo = '.b'
    s,m,c,k = featuresplot(sig, rate, typo)
    dataset.append(['trumpet',s,m,c,k])

print ("\npiano:"),
for i in range(1,46):
    print (i),
    file = 'Piano/sample_'+str(i)+'.wav'
    sig, rate = get_audio(file)
    typo = '.g'
    s,m,c,k = featuresplot(sig, rate, typo)
    dataset.append(['piano',s,m,c,k])

print ("\nflute:"),
for i in range(1,58):
    print (i),
    file = 'Flute/sample_'+str(i)+'.wav'
    sig, rate = get_audio(file)
    typo = '.r'
    s,m,c,k = featuresplot(sig, rate, typo)
    dataset.append(['flute',s,m,c,k])
print ("\nTraining Completed")

with open ('sample_data.pkl','wb') as pickle_file:
    pickle.dump(dataset, pickle_file)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

print ("Training the dataset")
dataset = np.array(dataset)
le = LabelEncoder()
data = pd.DataFrame(dataset)
X, Y = data.iloc[:,1:], dataset[:,0]
Y = le.fit_transform(Y)
lst = le.classes_

#print (X[:5])
#print (X.shape, Y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 42)

print (X_train.shape, y_train.shape)
clf = svm.SVC(kernel = 'linear', C = 3.0)
clf.fit(X_train, y_train)
acc = clf.score(X_test, y_test)
y_predict = clf.predict(X_test)
print (str(acc*100)+"% accuracy")
print (confusion_matrix(y_test, y_predict))

file= 'violin/sample_'+'3'+'.wav'
audio_file = wave.open(file)
length = audio_file.getnframes()
signal = np.zeros(length)

for i in range (0,length):
    data = audio_file.readframes(1)
    data = struct.unpack("<h", data)
    signal[i] = int(data[0])

rate = audio_file.getframerate()

signal = np.divide(signal, float(2**15))


plt.ylabel('mean_mfcc')
plt.xlabel('centroid')
#plt.axis([-100,100,-50,25])
plt.show()
