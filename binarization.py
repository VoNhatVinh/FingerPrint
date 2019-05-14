import numpy as np
from copy import deepcopy

def cnt_not_below(img, value):
    w, h = img.shape
    cnt = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] >= value:
                cnt += 1
    return cnt


def cnt_below(img, value):
    w, h = img.shape
    cnt = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] < value:
                cnt += 1
    return cnt


def get_mean_not_below(img, value):
    w, h = img.shape
    res = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] >= value:
                res += img[i, j]
    return res/cnt_not_below(img, value)


def get_mean_below(img, value):
    w, h = img.shape
    res = 0
    for i in range(w):
        for j in range(h):
            if img[i, j] < value:
                res += img[i, j]
    return res/cnt_below(img, value)


def get_var_not_below(img, value):
    w, h = img.shape
    variance = 0
    m = get_mean_not_below(img, value)
    for i in range(w):
        for j in range(h):
            if img[i, j] >= value:
                variance += (img[i, j] - m)**2
    return variance/cnt_not_below(img, value)


def get_var_below(img, value):
    w, h = img.shape
    variance = 0
    m = get_mean_not_below(img, value)
    for i in range(w):
        for j in range(h):
            if img[i, j] < value:
                variance += (img[i, j] - m)**2
    return variance/cnt_not_below(img, value)

def get_threshold(img):
    w, h = img.shape
    threshold = 0
    min_value = cnt_not_below(img, 0)*get_var_not_below(img, 0)/(w*h)
    for i in range(1, 256):
        value = cnt_below(img, i)*get_var_below(img, i)+cnt_not_below(img, i)*get_var_not_below(img, i)
        value = value/(w*h)
        if value < min_value:
            threshold = i
            min_value = value
    return threshold

def binary_image(img, threshold = -1):
    res = deepcopy(img)
    if threshold < 0:
        threshold = get_threshold(res)
    w, h = img.shape
    for i in range(w):
        for j in range(h):
            if res[i, j] > threshold:
                res[i, j] = 255
            else: res[i, j] = 0
    return res