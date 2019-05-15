import math
import numpy as np
from copy import deepcopy

def getMean(img):
    '''Hàm tính trung vị ảnh đã gray scale'''
    mean = 0
    w, h = img.shape
    for i in range(w):
        for j in range(h):
            mean += img[i, j]
    return mean/(w*h)

def getVariance(img, _mean):
    '''Hàm tính phương sai ảnh đã gray scale dựa vào tham số là trung vị'''
    variance = 0
    w, h = img.shape
    for i in range(w):
        for j in range(h):
            variance += (img[i,j] - _mean)**2
    return variance/(w*h)

def normalize(img, nMean, nVar):
    '''Hàm để chuẩn hóa img đã gray scale từ trung vị và phương sai cũ 
    thành trung vị mới là nMean và phương sai mới là nVar'''
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