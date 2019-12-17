# Run : python 4_masking.py -i pupper.jpg
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())  # this is  dictionary!

'''
Using a mask allows us to focus only on the portions of
the image that interests us.
'''
# load the image
image = cv2.imread(args["image"])  # returns a numpy array with image data
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (20,20), (150,150), 255, -1)
cv2.imshow("Mask", mask)

cv2.imshow("Bitwise and", cv2.bitwise_and(image, image, mask=mask))

cv2.waitKey(0)