import numpy as np
import cv2

def grayscale(img):
    '''Hàm trả về mảng 1D là pixel ở dạng gray scale'''
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def grayscale_lib(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)