# Run : python 4_splitting_and_merging.py -i pupper.jpg
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

''' We can split an image into its respective components'''
B, G, R = cv2.split(image)
# cv2.imshow("Red", R)
# cv2.imshow("Green", G)
# cv2.imshow("Blue", B)  # if dark, means it has lesser blue components in it
# cv2.waitKey(0)
# better visual if we set all the pixels *but* the current channel as 0
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
