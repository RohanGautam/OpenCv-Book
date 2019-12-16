import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args()) # this is  dictionary!
# load the image
image = cv2.imread(args["image"]) # returns a numpy array with image data
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2])) # 3 here for R,G,B

cv2.imshow("Image", image)
cv2.waitKey(0) # pauses program execution until any key is pressed
cv2.imwrite("newpupper.png", image)