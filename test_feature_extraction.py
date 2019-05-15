import cv2
import numpy as np
from grayscale import grayscale
from normalize import normalize
from orientation import orientation_estimation
from enchanted import gabor_filter
from binarization import binary_image
from thinning import Zhang_Suen_thinning
from thining_new import thinning
from minutiae import minutiae_extraction_filter

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
binary = binary_image(gabor, 0)
print("Done - binary image!!")
print("Thinning Image...")
thinned = thinning(binary)
print("Done - thinning!!!")
print("Minutiae Extracting...")
print(binary)
list_minutiae = minutiae_extraction_filter(thinned)
print(type(list_minutiae))
print("Done - minutiae extract!!")
w, h = gray.shape
minutiae_img = np.zeros((w, h))
for i in range(len(list_minutiae)):
    minutiae_img[list_minutiae[i][0], list_minutiae[i][1]] = 255

print(list_minutiae)
print(len(list_minutiae))
cv2.imshow('thinned image', thinned)
cv2.imshow('minutiae image', minutiae_img)

cv2.waitKey(0)