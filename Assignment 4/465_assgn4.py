"""
Roman Melnik - 2693934
CIS 465 - Professor Essa
Assignment 4
"""

import cv2 as cv
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
np.seterr(divide='ignore', invalid='ignore')

img = cv.imread("Image-1.bmp")
height, width, _ = img.shape
cv.imshow("original img", img)
height, width, _ = img.shape
grayImg = np.zeros((height, width), np.uint8)

def NTSCGrayscaleConversion(img):
    for i in range(0, height):
        for j in range(0, width):
            grayImg[i, j] = ((img[i,j][0] * 29.071)
                    + (img[i,j][1] * 149.685)
                    + (img[i,j][2] * 76.245)) / 255


NTSCGrayscaleConversion(img)
normalizedImg = grayImg / 255
normalizedImg.flatten()
hist, bins = np.histogram(normalizedImg, bins=256, range=(0,255))
cdf = hist.cumsum() / np.sum(hist)


def getL(cdfArray):
    for i in range(0, len(cdfArray)):
        if cdfArray[i] > 0.1:
            L = cdfArray[i]
            break
    return L


L = getL(cdf)
print('L is: ', L)

if L <= 50:
    z = 0
elif 50 < L <= 150:
    z = (L-50)/100
else:
    z = 1

print('z is: ', z)

luminanceEnhancedImg = (normalizedImg**(0.75 * z + 0.25) + ((1 - normalizedImg) * 0.4 * (1 - z)) + normalizedImg**(2-z)) / 2

convolutedImg = gaussian_filter(grayImg, sigma=30)
globalStandardDev = np.std(img)
print('global standard deviation: ', globalStandardDev)

if globalStandardDev <= 3:
    p = 3
elif 3 < globalStandardDev < 10:
    p = (27 - 2 * globalStandardDev) / 7
elif globalStandardDev >= 10:
    p = 1

print('p is: ', p)

E = (convolutedImg / grayImg)**p
contrastEnhancedImg = 255 * luminanceEnhancedImg**E

blueValues = np.zeros((height, width), np.uint8)
greenValues = np.zeros((height, width), np.uint8)
redValues = np.zeros((height, width), np.uint8)

for i in range(0, height):
    for j in range(0, width):
        blueValues[i, j] = img[i, j][2]
        greenValues[i, j] = img[i, j][1]
        redValues[i, j] = img[i, j][0]

myLambda = 0.8

colorRestoredImgBlue = contrastEnhancedImg * (blueValues / grayImg) * myLambda
colorRestoredImgGreen = contrastEnhancedImg * (greenValues / grayImg) * myLambda
colorRestoredImgRed = contrastEnhancedImg * (redValues / grayImg) * myLambda

colorRestoredImg = np.zeros_like(img)
for i in range(0, height):
    for j in range(0, width):
        colorRestoredImg[i, j][0] = colorRestoredImgBlue[i, j]
        colorRestoredImg[i, j][1] = colorRestoredImgGreen[i, j]
        colorRestoredImg[i, j][2] = colorRestoredImgRed[i, j]


output = Image.fromarray(colorRestoredImg)
output.save('output.jpg')
outputImg = cv.imread('output.jpg')
cv.imshow('output', outputImg)


cv.waitKey(0)
cv.destroyAllWindows()