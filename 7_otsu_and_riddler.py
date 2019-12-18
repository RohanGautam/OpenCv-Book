# Run : python 7_otsu_and_riddler.py -i coins.png
import numpy as np
import argparse
import mahotas
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# to remove high frequency edges we are not concerned with
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

'''Otsu and riddler method:
    Assumes there are 2 peaks in greyscale histogram. 
    It then attemts to find a `T` to seperate the two.
'''
T = mahotas.thresholding.otsu(blurred)
t_img = image.copy()
t_img[t_img > T] = 255 # everything more than thresh is white
t_img[t_img < 255] = 0 # if not white, make it black (region of intresr)
t_img = cv2.bitwise_not(t_img) # flip it and make region of intrest white instead, so we can potentially use it as a mask
cv2.imshow("Otsu", t_img)

T = mahotas.thresholding.rc(blurred)
t_img = image.copy()
t_img[t_img > T] = 255
t_img[t_img < 255] = 0
t_img = cv2.bitwise_not(t_img)
cv2.imshow("Riddler-calvard", t_img)

cv2.imshow("Riddler mask", cv2.bitwise_and(image, t_img))
cv2.waitKey(0)
