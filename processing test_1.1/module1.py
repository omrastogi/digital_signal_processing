#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     18-11-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

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
        mid = maxm/4
        for i in range(0, len(cnt)):
            if array[cnt[i]] > mid:
                imax = cnt[i]
                break
    return imax

import numpy as np
import matplotlib.pyplot as plt
array = [0,1,0,3,0,1,2,3,5,8,15,4,3,2,2,0,2,2,3,4,4,5,5,6,6,10,20,7,6,5,4,3,0,0,3,7,19,11,5,2,0]
imax=find_peak(array)
print imax
plt.plot(array)
plt.show()