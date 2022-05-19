"""
Roman Melnik - 2693934
CIS 465 - Professor Essa
Assignment 5
"""
import cv2 as cv
import numpy as np

#import video
video = cv.VideoCapture("basketball.avi")
totalFrames = int(video.get(cv.CAP_PROP_FRAME_COUNT))

success,image = video.read()

#convert to grayscale and put frames into arrays
#one array is for original rgb frames to fetch them at the end when we are writing the new video
#other array is for grayscale frames to do further calculations
grayFrames = []
rgbFrames = []
while True:
    success, image = video.read()
    if success:
        rgbFrames.append(image)
        grayFrame = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        grayFrames.append(grayFrame)
    else:
        break


#get the difference of frame1 and frame2
def getDifference(f2, f1):
    difference = np.sum(f2 - f1)
    return difference


#find key frames by calculating T and then comparing all values in data[] with T
keyFrames = []
def getKeyFrames(data, incrementer):
    beta = 0.5
    T = np.average(data) + beta * np.std(data)
    print('T: ', T)
    for i in range(0, len(data)):
        if data[i] > T:
            keyFrames.append(i + incrementer)


#create batches of 145 frames
d = []
incrementer = 0
for i in range(0, 2):
    for j in range(0, len(grayFrames[i]) - 1):
        v = getDifference(grayFrames[j+1], grayFrames[j])
        if len(d) == 145:
            getKeyFrames(d, incrementer)
            incrementer += 145
            print('d: ',d)
            d.clear()
        d.append(v)

print('key frames: ', keyFrames)
print('# of key frames: ', len(keyFrames))

#write video
videoOut = cv.VideoWriter('assgn5output.avi', 0x7634706d, 30, (400,300))
for i in range(0, len(keyFrames)):
    frameToFetch = keyFrames[i]
    frame = rgbFrames[frameToFetch]
    frame = cv.resize(frame, (400, 300))
    videoOut.write(frame)

#writing 3 key frames to show as examples in submission
frameSample = rgbFrames[74]
frameSample = cv.resize(frameSample, (400, 300))
keyFrameEx1 = cv.imwrite('key frame 74.jpg', frameSample)

frameSample = rgbFrames[314]
frameSample = cv.resize(frameSample, (400, 300))
keyFrameEx3 = cv.imwrite('key frame 314.jpg', frameSample)

frameSample = rgbFrames[699]
frameSample = cv.resize(frameSample, (400, 300))
keyFrameEx3 = cv.imwrite('key frame 699.jpg', frameSample)

videoOut.release()