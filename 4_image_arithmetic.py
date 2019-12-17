# Run : python 4_image_arithmetic.py -i pupper.jpg
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())  # this is  dictionary!
# load the image
image = cv2.imread(args["image"])  # returns a numpy array with image data
# cv2.imshow("Original", image)
''' Image arithmetic!
> `cv2.add()` clips at end, wehere as adding with numpy "wraps" it around, ie, has modulo-like behaviour 
What to you use depends on what you want'''
M = np.ones(image.shape, dtype="uint8") * 100 # every element is a hundred
# increasing/decreasing img's individual pixel intensity
# cv2.imshow("Added", cv2.add(image, M))
# cv2.imshow("Subtracted", cv2.subtract(image, M))

'''bitwise operations
We're not using RGB here, greyscale insteas
pixel is "on" if value >0 
pixel is "off" if value = 0 (black)
'''
white = 255
rectangle = np.zeros((300, 300), dtype = "uint8") # dont have rgb channel, hence not 300,300,3
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8") # dont have rgb channel, hence not 300,300,3
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
