import cv2
import numpy
#Roman Melnik - 2693934
#CIS 465 - Professor Essa
#Assignment 2 - Problem 3


#problem 3 part a
img = cv2.imread("tree.png", 0)
height, width = img.shape


cv2.imshow("part a - img before", img)
for i in range(0, height-1):
     for j in range(0, width-1):
         pixel = img[i, j]
         if pixel < 70:
             pixel = 0
             img[i, j] = pixel
         elif pixel >= 170:
             pixel = 255
             img[i, j] = pixel

cv2.imshow('part a - img after', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#problem 3 part b
img2 = cv2.imread("tree.png", 0)

cv2.imshow('part b - img before', img2)
for i in range(0, height - 1):
    for j in range(0, width -1):
        pixel = img2[i, j]
        if pixel < 70:
            pixel = 0
            img2[i, j] = pixel
        elif ((70 <= pixel) and (pixel <= 170)):
            pixel = pixel
            img2[i, j] = pixel
        elif pixel >= 170:
            pixel = 0
            img2[i, j] = pixel

cv2.imshow("part b - img after", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#problem 3, part c
img3 = cv2.imread("tree.png", 0)

cv2.imshow("part c - img before", img3)

numpy.seterr(divide='ignore')
c = 255 / numpy.log(1 + numpy.max(img3))
logImg = c * (numpy.log(1 + img3))

logImg = numpy.array(logImg, dtype=numpy.uint8)

cv2.imshow("part c - img after", logImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#problem 3, part d
img4 = cv2.imread("tree.png", 0)

cv2.imshow("part d - img before", img4)

for gamma in [0.5, 1.1, 1.6, 2.2]:
    gammaImg = numpy.array(255*(img4 / 255) ** gamma, dtype=numpy.uint8)
    cv2.imshow("part d - image after "+str(gamma)+" gamma correction", gammaImg)
    cv2.waitKey(0)

cv2.destroyAllWindows()
