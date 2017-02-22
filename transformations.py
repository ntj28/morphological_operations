import cv2
import numpy as np
import os

img = cv2.imread('original.png',0)

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
outputFilename= os.path.join(os.getcwd(),"output/erosion.png")
cv2.imwrite(outputFilename,erosion)

dilation = cv2.dilate(img,kernel,iterations = 1)
outputFilename= os.path.join(os.getcwd(),"output/dilation.png")
cv2.imwrite(outputFilename,dilation)

img1 = cv2.imread('open.png',0)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
outputFilename= os.path.join(os.getcwd(),"output/opening.png")
cv2.imwrite(outputFilename,opening)

img2 = cv2.imread('close.png',0)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
outputFilename= os.path.join(os.getcwd(),"output/closing.png")
cv2.imwrite(outputFilename,closing)


gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
outputFilename= os.path.join(os.getcwd(),"output/gradient.png")
cv2.imwrite(outputFilename,gradient)

kerneltop= np.ones((9,9),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kerneltop)
outputFilename= os.path.join(os.getcwd(),"output/tophat.png")
cv2.imwrite(outputFilename,tophat)


blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
outputFilename= os.path.join(os.getcwd(),"output/blackhat.png")
cv2.imwrite(outputFilename,blackhat)
