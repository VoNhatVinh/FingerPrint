import numpy as np
import math


'''
Create a mask for gabor filter.

Parameter
----
direct: float
        direction of current fingerprint point
widSquare: int
		   1/2 kernala Size.
	  
Return
----
direct: float
		direction of fingerprint
'''
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


	
'''
Image filtered by Gabor

Parameter
----
image : 2D-array.
        gray image
direct: float
        direction of current fingerprint point
widSquare: int
		   1/2 kernala Size. 
f:  float
	the cycle of cos
fi: float
	standard deviation Gauss
	  
Return
----
gabor: 2D-array
	   the image filtered by Gabor
'''
def gabor_filter(image, direct, widSquare, f, fi):
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