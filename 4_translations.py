# Run : python 4_translations.py -i pupper.jpg
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())  # this is  dictionary!
# load the image
image = cv2.imread(args["image"])  # returns a numpy array with image data
cv2.imshow("Original", image)

shifted = imutils.translate(image, -30, 40)
cv2.imshow("Translated", shifted)

shifted = imutils.rotate(image, -35, scale=0.5) # halves size of image
cv2.imshow("Rotated", shifted)

shifted = imutils.resize(image,width = 180)
cv2.imshow("Resized w aspect ratio", shifted)

shifted = imutils.flip(image, horizontally=True)
cv2.imshow("Flipped horiz", shifted)
shifted = imutils.flip(image, vertically=True)
cv2.imshow("Flipped vert", shifted)
shifted = imutils.flip(image, horizontally=True, vertically=True)
cv2.imshow("Flipped both", shifted)

# cropping image uses numpy slices