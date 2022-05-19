"""
Roman Melnik - 2693934
CIS 465 - Dr. Essa
FINAL EXAM
12/10/2021
"""
import matplotlib.pyplot as plt
import numpy
import numpy as np
import cv2 as cv
import math

import scipy.signal
from PIL import Image


#load images
I = np.load('FE_Data.npy')
img1 = I[0]
img2 = I[1]
cv.imshow('input', img1)
cv.waitKey(0)
cv.destroyAllWindows()


#write kernels
k1 = np.array([[1, math.sqrt(2), 1], [0, 0, 0], [-1, -math.sqrt(2), -1]])
k2 = np.array([[1, 0, -1], [math.sqrt(2), 0, -math.sqrt(2)], [1, 0, -1]])
k3 = np.array([[0, -1, math.sqrt(2)], [1, 0, -1], [-math.sqrt(2), 1, 0]])
k4 = np.array([[math.sqrt(2), -1, 0], [-1, 0, 1], [0, 1, -math.sqrt(2)]])
k5 = np.array([[0, 1, 0], [-1, 0, -1], [0, 1, 0]])
k6 = np.array([[-1, 0, 1], [0, 0, 0], [1, 0, -1]])
k7 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
k8 = np.array([[-2, 1, -2], [-2, 4, -2], [1, -2, 1]])
k9 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


#perform operations and display 3x3 plot

f, axarr = plt.subplots(3,3)

g1 = scipy.signal.convolve(img1, k1, mode='full', method='auto')
axarr[0,0].imshow(g1, cmap='gray')

g2 = scipy.signal.convolve(img1, k2, mode='full', method='auto')
axarr[0,1].imshow(g2, cmap='gray')

g3 = scipy.signal.convolve(img1, k3, mode='full', method='auto')
axarr[0,2].imshow(g3, cmap='gray')

g4 = scipy.signal.convolve(img1, k4, mode='full', method='auto')
axarr[1,0].imshow(g4, cmap='gray')

g5 = scipy.signal.convolve(img1, k5, mode='full', method='auto')
axarr[1,1].imshow(g5, cmap='gray')

g6 = scipy.signal.convolve(img1, k6, mode='full', method='auto')
axarr[1,2].imshow(g6, cmap='gray')

g7 = scipy.signal.convolve(img1, k7, mode='full', method='auto')
axarr[2,0].imshow(g7, cmap='gray')

g8 = scipy.signal.convolve(img1, k8, mode='full', method='auto')
axarr[2,1].imshow(g8, cmap='gray')

g9 = scipy.signal.convolve(img1, k9, mode='full', method='auto')
axarr[2,2].imshow(g9, cmap='gray')

plt.show()

#part 3
part3 = np.sqrt((g1**2 + g2**2 + g3**2 + g4**2) / (g1**2 + g2**2 + g3**2 + g4**2 + g5**2 + g6**2 + g7**2 + g8**2 + g9**2))
cv.imshow('part3', part3)

#padding matrix - this is my code from assignment 1
def pad_matrix(matrix, n=None, l=None):
    temp = []
    if l is None:
        for i in range(n + 2):
            temp.append(0)
        matrix.append(temp)
    else:
        temp.append(0)
        for j in l:
            temp.append(j)
        temp.append(0)
        matrix.append(temp)

rows = len(part3)
columns = len(part3[0])

userMatrix = []
pad_matrix(n=columns, matrix=userMatrix)
for i in range(0, rows):
    tempRow = []
    tempRow.append(0)
    for j in range(0, columns):
        value = part3[i,j]
        tempRow.append(value)
    tempRow.append(0)
    userMatrix.append(tempRow)
pad_matrix(n=columns, matrix=userMatrix)


answer = []
for i in range(1, rows + 1):
    myRow = []
    for j in range(1, columns + 1):

        currentPosition = userMatrix[i][j]

        rightValue = userMatrix[i][j+1] - currentPosition
        topRightValue = userMatrix[i-1][j+1] - currentPosition
        topValue = userMatrix[i-1][j] - currentPosition
        topLeftValue = userMatrix[i-1][j-1] - currentPosition
        leftValue = userMatrix[i][j-1] - currentPosition
        bottomLeftValue = userMatrix[i+1][j-1] - currentPosition
        bottomValue = userMatrix[i+1][j] - currentPosition
        bottomRightValue = userMatrix[i+1][j+1] - currentPosition

        # performing steps 2, 3, and 4 of the 6 step process
        # if else statements check if the value is positive or negative
        # if the value is positive, the value should be reassigned to one
        # however, we skip this step and reassign the value to the corresponding decimal value
        if rightValue >= 0:
            rightValue = 1
        else:
            rightValue = 0

        if topRightValue >= 0:
            topRightValue = 2
        else:
            topRightValue = 0

        if topValue >= 0:
            topValue = 4
        else:
            topValue = 0

        if topLeftValue >= 0:
            topLeftValue = 8
        else:
            topLeftValue = 0

        if leftValue >= 0:
            leftValue = 16
        else:
            leftValue = 0

        if bottomLeftValue >= 0:
            bottomLeftValue = 32
        else:
            bottomLeftValue = 0

        if bottomValue >= 0:
            bottomValue = 64
        else:
            bottomValue = 0

        if bottomRightValue >= 0:
            bottomRightValue = 128
        else:
            bottomRightValue = 0

        sum = rightValue + topRightValue + topValue + topLeftValue + leftValue + bottomLeftValue + bottomValue + bottomRightValue
        myRow.append(sum)
    answer.append(myRow)

#convert to numpy array
answerArr = np.array(answer)

cv.imshow('part 4', np.uint8(answerArr))
part4 = np.uint8(answerArr)

##############################
# i could not get a 1x3 plot at the end as there were some issues, and also running out of time
##########################

cv.waitKey(0)
cv.destroyAllWindows()