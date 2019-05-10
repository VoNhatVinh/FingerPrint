import cv2
from grayscale import grayscale
from normalize import normalize
from orientation import orientation_estimation

a = cv2.imread('1_1.bmp')
gray = grayscale(a)
normal = normalize(gray, 50, 300)

a[:, :, 0] = a[:, :, 1] = a[:, :, 2] = normal

direct = orientation_estimation(normal)