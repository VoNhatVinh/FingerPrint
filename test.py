import cv2
from grayscale import grayscale
from normalize import normalize
from orientation import orientation_estimation
from enchanted import gabor_filter
from binarization import binary_image

from grayscale import grayscale_lib
from enchanted import gabor_filter_lib

# Non-library function
a = cv2.imread('1_1.bmp')
gray = grayscale(a)
normal = normalize(gray, 50, 300)

print("Estimating Orientation...")
direct = orientation_estimation(normal)
print("Orientation Estimation Done!!")
print("Gabor filter in image...")
gabor = gabor_filter(normal, direct, 4, 1/7, 3)
print("Gabor filter done!!")
print("Binary image...")
binary = binary_image(gabor, 30)
print("Done - binary image!!")
cv2.imshow('gabor', gabor)
cv2.imshow('binary', binary)
cv2.waitKey(0)

# Using library function, cái này đang bị lỗi(hàm gabor_filter_lib), với
# hàm orentiation estimation đang xài vòng lặp

'''
img = cv2.imread('1_1.bmp')
gray = grayscale_lib(img)
normal = normalize(gray, 50, 300)
print("Orientation Estimation...")
direct = orientation_estimation(normal)
print("Done - Estimation!!")
print("Gabor filter...")
gabor = gabor_filter_lib(gray, direct, 4, 1/7, 3)
print("Done - Gabor!!!")
img[:,:,0] = img[:,:,1] = img[:,:,2] = gabor
cv2.imshow('normal image', normal)
cv2.imshow('gabor', img)
cv2.waitKey(0)
'''