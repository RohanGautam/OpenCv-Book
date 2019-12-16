# Run : python 2_getting_setting.py -i pupper.jpg
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args()) # this is  dictionary!
# load the image
image = cv2.imread(args["image"]) # returns a numpy array with image data
cv2.imshow("Original", image)

'''Opencv stored channels in reverse order: Blue, green, red'''
b, g, r = image[0, 0] # (0,0) is the top-left corner
print(f'R : {r}, G : {g}, B : {b}')

# changing the first pixel
image[0,0] = (255, 0, 0) # pure blue
b, g, r = image[0, 0] # (0,0) is the top-left corner
print(f'R : {r}, G : {g}, B : {b}')
# cv2.imshow("First pixel blue", image)

# changing topleft 100x100 pixel region
corner = image[0:200, 0:100] # first slice is for the rows, ie, the y axis
cv2.imshow("corner", corner)
image[0:200, 0:100] = (255, 0, 0) # pure blue
cv2.imshow("Updated", image)
cv2.waitKey(0)