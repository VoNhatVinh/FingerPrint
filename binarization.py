import numpy as np
from copy import deepcopy

'''
Count pixel which value not below value

Parameters
----
img: 2D-array.
     gray image
value: int

Return
----
cnt: int
     number of pixel that value not below value parameter.
'''
def cnt_not_below(img, value):
    w, h = img.shape
    cnt = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] >= value:
                cnt += 1
    return cnt


'''
Count pixel which value below value

Parameters
----
img: 2D-array.
     gray image
value: int

Return
----
cnt: int
     number of pixel that value below value parameter
'''
def cnt_below(img, value):
    w, h = img.shape
    cnt = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] < value:
                cnt += 1
    return cnt


'''
Get mean image which pixel value not below value

Parameters
----
img: 2D-array.
     gray image
value: int

Return
----
mean: float
      mean of a pixel that value not below value in parameter
'''
def get_mean_not_below(img, value):
    w, h = img.shape
    res = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] >= value:
                res += img[i, j]
    return res/cnt_not_below(img, value)


'''
Get mean image which pixel value below value

Parameters
----
img: 2D-array.
     gray image
value: int

Return
----
mean: float
      mean of a pixel that value below value in parameter
'''
def get_mean_below(img, value):
    w, h = img.shape
    res = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] < value:
                res += img[i, j]
    return res/cnt_below(img, value)


'''
Get variance image which pixel value not below value

Parameters
----
img: 2D-array.
     gray image
value: int

Return
----
variance: float
          variance of a pixel that value not below value in param
'''
def get_var_not_below(img, value):
    w, h = img.shape
    variance = 0
    m = get_mean_not_below(img, value)
    for i in range(w):
        for j in range(h):
            if img[i, j] >= value:
                variance += (img[i, j] - m)**2
    return variance/cnt_not_below(img, value)


'''
Get variance image which pixel value below value

Parameters
----
img: 2D-array.
     gray image
value: int

Return
----
variance: float
          variance of a pixel that value below value in parameter
'''
def get_var_below(img, value):
    w, h = img.shape
    variance = 0
    m = get_mean_not_below(img, value)
    for i in range(w):
        for j in range(h):
            if img[i, j] < value:
                variance += (img[i, j] - m)**2
    return variance/cnt_not_below(img, value)


'''
Compute threshold using Ostu algorithm

Parameters
----
img: 2D-array.
     gray image

Return
----
threshold: int
           threshold compute using Otsu algorithm
'''
def get_threshold(img):
    w, h = img.shape
    threshold = 0
    min_value = cnt_not_below(img, 0)*get_var_not_below(img, 0)/(w*h)
    for i in range(1, 256):
        value = cnt_below(img, i)*get_var_below(img, i) + \
            cnt_not_below(img, i)*get_var_not_below(img, i)
        value = value/(w*h)
        if value < min_value:
            threshold = i
            min_value = value
    return threshold

'''
Binarization Image

Parameters
----
img: 2D-array
     gray image

threshold: -1 (default)

Return
----
binary image: 2D-array
'''
def binary_image(img, threshold=-1):
    res = deepcopy(img)
    if threshold < 0:
        threshold = get_threshold(res)
    w, h = img.shape
    for i in range(w):
        for j in range(h):
            if res[i, j] > threshold:
                res[i, j] = 255
            else:
                res[i, j] = 0
    return res
