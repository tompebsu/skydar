import cv2
import numpy as np

frameWidth = 320
frameHeight = 240
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

#myColors = [[5,12,130,250,172,255]]
#target colors
blue = [96,94,77,146,173,255]
red = [0,97,145,14,171,255]
orange = [0,117,158,33,164,255]
flag = [5,130,172,12,250,255]
myColors = [blue,red,orange]

#BGR
blue_contour = [191,0,0]
red_countour =  [5,5,255]
orange_countour = [0,127,255]

myColorValues = [blue_contour,red_countour,orange_countour]

myPoints = []  #[x,y, colorId]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints =[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getCountours(mask)
        cv2.circle(imgResult, (x, y), 10,myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
       # cv2.imshow(str(color[1]),mask)
    return newPoints

def getCountours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10,myColorValues[point[2]], cv2.FILLED)



while True:
    success, img = cap.read()
    imgResult = img.copy()
    #findColor(img, myColors,myColorValues)
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    #cv2.imshow("Video", img)
    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break