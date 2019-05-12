import numpy as np


def create_list_neighbor(img, x, y):
    res = []
    res.append(img[x, y-1])
    res.append(img[x+1, y-1])
    res.append(img[x+1, y])
    res.append(img[x+1, y+1])
    res.append(img[x, y+1])
    res.append(img[x-1, y+1])
    res.append(img[x-1, y])
    res.append(img[x-1, y-1])
    return res


def getA(img, pList):
    cnt = 0
    for i in range(len(pList) - 1):
        cnt += (pList[i] == 255 and pList[i + 1] == 0)
    cnt += (pList[len(pList)-1] == 255 and pList[0] == 0)
    return cnt


def getB(img, pList):
    cnt = 0
    for i in range(len(pList)):
        if pList[i] == 0:
            cnt += 1
    return cnt


def Zhang_Suen_thinning(img):

    w, h = img.shape
    # Step 1:
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            pList = create_list_neighbor(img, i, j)
            if getA(img, pList) == 1 and 2 <= getB(img, pList) <= 6:
                if (pList[0] == 255 or pList[2] == 255 or pList[4] == 255) and (pList[2] == 255 or pList[4] == 255 or pList[6] == 255):
                    img[i, j] = 255

    # Step 2:
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            pList = create_list_neighbor(img, i, j)
            if getA(img, pList) == 1 and 2 <= getB(img, pList) <= 6:
                if (pList[0] == 255 or pList[2] == 255 or pList[6] == 255) and (pList[0] == 255 or pList[4] == 255 or pList[6] == 255):
                    img[i, j] = 255

    return img
