# Run : python 7_simple_thresholding.py -i coins.png
import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

'''Thresholding is binarization of an img. Pixel values of either 0 or 255'''

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# to remove high frequency edges we are not concerned with
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)
'''Simple thresholding: preovide a threshold value `T`. Below T ->0, above ->255'''
threshold = 155 
T, t_img = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold binary", t_img)
T, t_img_inv = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold binary inverse", t_img_inv)
# can use it as a mask!
cv2.imshow("Threshold binary inverse as mask", cv2.bitwise_and(image, t_img_inv))

cv2.waitKey(0)
