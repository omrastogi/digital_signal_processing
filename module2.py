from python_speech_features import mfcc
from python_speech_features import logfbank
from python_speech_features import ssc
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

mfcclst=[]
cent=[]



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
        slst.append(s[i][7])



    m=[]
    k=[]
    s=[]
    k.append(np.mean(klst))
    m.append(np.mean(mlst))
    s.append(np.mean(slst))

    clst=[]
    for i in range(0, len(fbank_feat)):
        l = m[0:4]
        clst.append(np.mean(fbank_feat[i]))
    c=[]
    c.append(np.mean(clst))
    plt.plot(m,c, typo)
    return  s[0],k[0],m[0],c[0]

mlst = []
clst = []
for i in range (1,8):
    (rate,sig) = wav.read('Piano/sample_'+str(i)+'.wav')
    typo = '.g'
    s,k,m,c = featuresplot(sig,rate,typo)
    mlst.append(s)
    clst.append(m)
    print s
'''
    m = mfcc(sig,rate)

    fbank_feat = logfbank(sig,rate)

    list = (fbank_feat[1:3,:])
    #print fbank_feat

    mlst = []
    for i in range(0, len(m)):
        mlst.append(np.mean(m[i]))
    mfcclst.append(np.mean(mlst))

    clst=[]
    for i in range(0, len(fbank_feat)):
        clst.append(np.mean(fbank_feat[i]))
    cent.append(np.mean(clst))
'''

print ("mfcc:/n",mlst)

print ("cent: /n",clst)
plt.subplot(111)
plt.plot(mlst, clst, '.b')
plt.ylabel('mean_mfcc')
plt.xlabel('mean_centeriod')
#plt.axis([-30,30,0,40])
plt.show()