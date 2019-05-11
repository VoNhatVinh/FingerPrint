import cv2
import numpy as np
import math


def create_mask(direct, widsquare, f, fi):
    '''Hàm tạo mặt nạ gabor,
    direct(scalar value) - Hướng để tính gabor mesh,
    widsquare(scalar value) - size của gabor [-widsquare, widsquare],
    fi là độ lệch chuẩn Gauss, f là chu kỳ hàm cos,
    Hàm trả về mặt nạ tìm được theo hướng direct'''

    mask = np.ones((2*widsquare + 1, 2*widsquare + 1))
    for i in range(2*widsquare + 1):
        for j in range(2*widsquare + 1):
            x = (i-widsquare)*math.cos(direct) + (j-widsquare)*math.sin(direct)
            y = -(i-widsquare)*math.sin(direct) + \
                (j-widsquare)*math.cos(direct)
            mask[i, j] = math.exp(-0.5*((x*x)/(fi*fi) + (y*y)/(fi*fi)))
            mask[i, j] *= math.cos(2*math.pi*f*x)
    return mask


def gabor_filter(image, direct, widSquare, f, fi):
    '''Hàm filter ảnh sử dụng gabor_filter.
    Tham số là image - mảng ảnh(1D - grayscale),
    mảng orientation - direct,
    width square là size của gabor,
    fi là độ lệch chuẩn Gauss, f là chu kỳ hàm cos.
    Hàm trả về mảng ảnh là ảnh đã được filter'''

    w, h = image.shape
    pointvalue = 0
    gabor = np.zeros((w, h))
    for x in range(w - 2*widSquare - 1):
        for y in range(h - 2*widSquare - 1):
            mask = create_mask(direct[x, y], widSquare, f, fi)
            for i in range(2*widSquare + 1):
                for j in range(2*widSquare + 1):
                    pointvalue += mask[i, j]*image[x+i, y+j]
            if pointvalue > 255:
                pointvalue = 255
            if pointvalue < 0:
                pointvalue = 0
            gabor[x, y] = pointvalue
    return gabor


def gabor_filter_lib(image, direct, widSquare, f, fi):

    w, h = direct.shape
    filter_img_all = np.zeros((w, h))
    for i in range(w):
        for j in range(h):
            g_kernel = cv2.getGaborKernel(
                (widSquare, widSquare), fi, direct[i, j], 10.0, 1/f, 0, ktype=cv2.CV_32F)
            filtered_img = cv2.filter2D(image, cv2.CV_8UC3, g_kernel)
            filter_img_all += filtered_img

    return filter_img_all
        