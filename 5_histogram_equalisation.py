from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
'''Histogram equalization improves the contrast of an image
by “stretching” the distribution of pixels.'''

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(image)
# `np.hstack` Stack arrays in sequence horizontally (column wise)
cv2.imshow("Histogram Equalization", np.vstack([image, eq]))

org_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist = cv2.calcHist([eq], [0], None, [256], [0, 256])
# make a figure
plt.figure()
# set title,x,y labels
plt.title("Before and after Histogram Equalization")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
# plot it
plt.plot(hist)
plt.plot(org_hist)

''' We see that hist equalisation spreads the peak from wherever it is'''
cv2.waitKey(0)
plt.show()

''' Can provide a mask to only analyse a region of the image that intrests us '''
