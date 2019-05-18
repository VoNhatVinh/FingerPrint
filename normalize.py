import math
import numpy as np
from copy import deepcopy


'''
Calculate mean of gray image

Parameter
----
img : 2D-array.
      gray image

Return
----
mean of image: int        
'''
def getMean(img):
    mean = 0
    w, h = img.shape

    for i in range(w):
        for j in range(h):
            mean += img[i, j]
    return mean/(w*h)



'''
Calculate variance of gray image

Parameters
----
img : 2D-array.
      gray image
_mean: double
       mean off gray image

Return
----
Variance of gray Image: float
'''
def getVariance(img, _mean):
    variance = 0
    w, h = img.shape

    for i in range(w):
        for j in range(h):
            variance += (img[i,j] - _mean)**2
    return variance/(w*h)



'''
Normalize image

Parameters
----
img  : 2D-array.
       gray image
nMean: double 
       mean
nVar : float
       variance

Return
----
normalized img: 2D-array 
'''
def normalize(img, nMean, nVar):
    
    w, h = img.shape
    _mean = getMean(img)
    var = getVariance(img, _mean)
    for i in range(w):
        for j in range(h):
            diff = math.fabs(img[i, j] - _mean)*math.sqrt(nVar/var)
            if img[i,j] > _mean:
                img[i, j] = nMean + diff
            else: img[i, j] = nMean - diff
    return img