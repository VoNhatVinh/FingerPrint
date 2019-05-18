import numpy as np

'''
Calculate mean of gray image

Parameter
----
img : 3D-array.
      original image 

Return
----
gray image: 2D-array       
'''
def grayscale(img):
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray