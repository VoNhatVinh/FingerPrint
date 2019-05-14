import cv2
import numpy as np


def isBoder(image, x, y):
    if (image[x - 1, y] == 255 or image[x + 1, y] == 255 or image[x, y - 1] == 255 or image[x, y + 1] == 255) and image[x, y] == 0:
        return True
    return False


def isDeleable(image, x, y):
    p1 = image[x - 1, y - 1]
    p2 = image[x, y - 1]
    p3 = image[x + 1, y - 1]
    p4 = image[x - 1, y]
    p5 = image[x + 1, y]
    p6 = image[x - 1, y + 1]
    p7 = image[x, y + 1]
    p8 = image[x + 1, y + 1]

    if (p1 + p2 + p3) == 0 and (p6 * p7 * p8) > 0:
        return True

    if (p1 + p2 + p4) == 0 and (p5 * p7 * p8) > 0:
        return True

    if (p1 + p4 + p6) == 0 and (p3 * p5 * p8) > 0:
        return True

    if p2 + p3 + p5 == 0 and p4 * p6 * p7 > 0:
        return True

    if p6 + p7 + p8 == 0 and p1 * p2 * p3 > 0:
        return True

    if p5 + p7 + p8 == 0 and p1 * p2 * p4 > 0:
        return True

    if p3 + p5 + p8 == 0 and p1 * p4 * p6 > 0:
        return True

    if p4 + p6 + p7 == 0 and p2 * p3 * p5 > 0:
        return True

    return False


def makeBone(image):
    height, width = image.shape
    isBone = False
    while not isBone:
        isBone = True
        for i in range(height - 1):
            for j in range(width - 1):
                if isBoder(image, i, j) and isDeleable(image, i, j):
                    image[i, j] = 255
                    isBone = False


def cleanBone(image):
    height, width = image.shape
    for i in range(height - 1):
        for j in range(width - 1):
            if image[i, j] == 0:
                if image[i - 1, j - 1] == 0:
                    image[i, j - 1] = 255
                    image[i - 1, j] = 255
                if image[i + 1, j - 1] == 0:
                    image[i, j - 1] = 255
                    image[i + 1, j] = 255
                if image[i + 1, j + 1] == 0:
                    image[i + 1, j] = 255
                    image[i, j + 1] = 255
                if image[i - 1, j + 1] == 0:
                    image[i - 1, j] = 255
                    image[i, j + 1] = 255

def thinning(image):
    makeBone(image)
    cleanBone(image)
    return image