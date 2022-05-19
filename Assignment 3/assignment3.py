# Roman Melnik - 2693934
# CIS 465 - Professor Essa
# Assignment 3

import cv2 as cv
from matplotlib import pyplot as plt


#part 1
#converting image from rgb to grayscale using average method
def rgbToGray(image, image2):
    cv.imshow("original img", image)
    height, width, _ = image.shape
    for i in range(0, height ):
        for j in range(0, width):
            pixel = image[i, j]
            pixel = (pixel[0] / 3) + (pixel[1] / 3) + (pixel[2] / 3)
            image[i, j] = pixel

    cv.imshow("image to grayscale", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    #pass color and grayscale images to histogram function
    histogram(image2, image)

#part 2
#displaying histograms for the color and grayscale images
def histogram(colorImage, grayImage):
    blueValues = []
    greenValues = []
    redValues = []
    grayscaleValues = []

    #obtaining data for histograms
    height, width, _ = grayImage.shape
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            grayscaleValues.append(grayImage[i, j, 0])
            blueValues.append(colorImage[i, j, 0])
            greenValues.append(colorImage[i, j, 1])
            redValues.append(colorImage[i, j, 2])

    #creating histogram for color image
    plt.subplot(1, 2, 1).title.set_text('Color Image Intensity')
    plt.hist(blueValues, bins=256, alpha=0.5, color='blue', label='Blue Values')
    plt.hist(greenValues, bins=256, alpha=0.5, color='green', label='Green Values')
    plt.hist(redValues, bins=256, alpha=0.5, color='red', label='Red Values')
    plt.legend(loc='upper right')
    plt.xlabel("RGB Values")
    plt.ylabel("Value Frequency")

    #creating histogram for grayscale image
    plt.subplot(1, 2, 2).title.set_text('Grayscale Image Intensity')
    plt.hist(grayscaleValues, bins=256, color='gray', label='Values')
    plt.legend(loc='upper right')
    plt.xlabel("Values")
    plt.ylabel("Value Frequency")

    plt.suptitle("Intensity Histograms Before Equalization")
    plt.show()


#part 3
#creating function to equalize image and display the histogram
def equalizer(image):
    imgValuesBefore = []
    imgValuesAfter = []
    height, width, _ = image.shape

    #obtaining data for histogram before equalizing image
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            imgValuesBefore.append(image[i, j, 0])

    #equalizing image
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('before equalize', image)
    equalizedImage = cv.equalizeHist(image)
    cv.imshow('after equalize', equalizedImage)
    cv.waitKey(0)
    cv.destroyAllWindows()

    #obtaining data for histogram after equalizing image
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            imgValuesAfter.append(equalizedImage[i, j])

    #creating each histogram
    plt.subplot(1, 2, 1).title.set_text('Before Equalization')
    plt.hist(imgValuesBefore, bins=256, color='gray')
    plt.xlabel('Values')
    plt.ylabel('Values Frequency')

    plt.subplot(1, 2, 2).title.set_text('After Equalization')
    plt.hist(imgValuesAfter, bins=256, color='gray')
    plt.xlabel('Values')
    plt.ylabel('Values Frequency')

    #title and display histogram
    plt.suptitle("Intensity Histograms After Equalization")
    plt.show()


def main():
    #enter image name of image to process
    img = cv.imread("overSatImg.jpg")
    img2 = cv.imread("overSatImg.jpg")
    rgbToGray(img, img2)
    equalizer(img)


if __name__ == '__main__':
    main()
