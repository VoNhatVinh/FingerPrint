import numpy as np

'''
Get eucleur distance between a and b

Parameters:
----
a: 1D-array.
   a[0] is x cordinate of a.
   a[1] is y cordinate of a.
b: 1D-array.
   b[0] is x cordinate of b.
   b[1] is y cordinate of b.

Return:
----
Distance based on Euclid between a and b.
'''
def distance(a, b):
    return (a[0] - b[0])**2 + (b[1] - a[1])**2



'''
Check if pixel at (x_cor, y_cor) is a feature

Parameters:
----
img:   2D-array.
       gray image.

x_cor: int.
       x cordinate of pixel.

y_cor: int.
       y cordinate of pixel.

Return:
----
True if pixel at (x_cor, y_cor) is minutiae.
False if pixel at (x_cor, y_cor) isn't minutiae.
'''
def is_feature(img, x_cor, y_cor):
    w, h = img.shape
    if x_cor > 0 and x_cor < w - 1 and y_cor > 0 and y_cor < h - 1 and img[x_cor, y_cor] == 0:
        result = abs(img[x_cor - 1, y_cor - 1] - img[x_cor - 1, y_cor]) + abs(img[x_cor - 1, y_cor + 1] - img[x_cor, y_cor + 1]) + abs(img[x_cor + 1, y_cor + 1] - img[x_cor + 1, y_cor]) + abs(img[x_cor + 1, y_cor - 1] - img[x_cor, y_cor - 1])
        
        if result == 255 or result == 3*225:
            return True
    return False




'''
Minutiae Extraction From image

Parameters:
----
img: 2D-array
     thinned image

Return:
----
minutiae_list: list
               minutiae list extracted from image
'''
def minutiae_extraction(img):
    minutiae_list = []
    w, h = img.shape
    for i in range(50, w - 50):
        for j in range(20, h - 20):
            if is_feature(img, i, j):
                minutiae_list.append([i, j])
    return minutiae_list



'''
Filter minutiae after extract

Parameter:
----
list_minutiae: list
               list minutiae after extraction

Return:
----
filter: list
        list minutiae after filter
'''
def filter_minutiae(list_minutuae):
    m = len(list_minutuae)
    a = np.ones((1, m))
    for i in range(m - 1):
        for j in range(i + 1, m):
            if a[0, i] == 1 and a[0, j] == 1 and distance(list_minutuae[i], list_minutuae[j]) < 36:
                a[0, i] = 0
                a[0, j] = 0
                break
    
    filter = []
    for i in range(m):
        if a[0, i] == 1:
            filter.append(list_minutuae[i])
    return filter



'''
Minutiae Extraction and Filter from Image

Parameters:
----
img: 2D-array
     thinned image

Return:
----
mList: list
       list minutiae after filter
'''
def minutiae_extraction_filter(img):
    mList = minutiae_extraction(img)
    mList = filter_minutiae(mList)
    return mList
