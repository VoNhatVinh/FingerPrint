import numpy as np
import math

'''
Sobel mask
-1 -2 -1
 0  0  0
 1  2  1
 
Parameter
----
img : 2D-array.
      gray image
i, j: the current index

Return
----
Sobel mask in horizontal: 2D-array      
'''
def sobelY(image, i, j):
    return image[i + 2, j] + 2 * image[i + 2, j + 1] + image[i + 2, j + 2] - image[i, j] - 2 * image[i, j + 1] - image[i, j + 2]

	

'''
Sobel mask
-1  0 -1
-2  0 -2
-1  0 -1
 
Parameter
----
img : 2D-array.
      gray image
i, j: the current index

Return
----
Sobel mask in vertical: 2D-array      
'''
def sobelX(image, i, j):
    return image[i, j + 2] + 2 * image[i + 1, j + 2] + image[i + 2, j + 2] - image[i, j] - 2 * image[i + 1, j] - image[i + 2, j]


'''
Find the direction.

Parameter
----
img : 2D-array.
      gray image
wS	: int
	  kernel size.
	  
Return
----
direct: float
		direction of fingerprint
'''
def orientation_estimation(img, wS=4):
    width, height = img.shape
    direct = np.zeros((height, width))
	
    for i in range(wS + 1, width - wS - 1):
        for j in range(wS + 1, height - wS - 1):
            gXX = gXY = gYY = 0
            for k in range(i - wS, i + wS - 1):
                for l in range(j - wS, j + wS - 1):
                    gX = sobelX(img, k, l)
                    gY = sobelY(img, k, l)
                    gXX += gX*gX
                    gXY += gX*gY
                    gYY += gY*gY
            direct[i, j] = math.pi/2 - 0.5*math.atan2(2*gXY,gXX-gYY)
            
    return direct