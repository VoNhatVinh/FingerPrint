import cv2
import numpy as np
from grayscale import grayscale
from normalize import normalize
from orientation import orientation_estimation
from enchanted import gabor_filter
from binarization import binary_image
from thining_new import thinning
from minutiae import minutiae_extraction_filter



'''
Preprocess image include: grayscale, normalize, gabor_filter, binarization, minutiae

Parameters
----
img  : 2D-array.
       gray image

Return
----
preprocessed imaged 
'''
def preprocess(img_path):
  print("Preprocess in image: ", img_path)
  a = cv2.imread(img_path)
  gray = grayscale(a)
  normal = normalize(gray, 50, 300)
  direct = orientation_estimation(normal)
  gabor = gabor_filter(normal, direct, 4, 1/7, 3)
  binary = binary_image(gabor, 50)
  thinned = thinning(binary)
  list_minutiae = minutiae_extraction_filter(thinned)
    
  w, h = gray.shape
  minutiae_img = np.zeros((w, h))    
  for i in range(len(list_minutiae)):
    minutiae_img[list_minutiae[i][0], list_minutiae[i][1]] = 1 #the minutiae point = 1, the others = 0

  return minutiae_img
