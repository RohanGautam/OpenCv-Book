# Run : python 7_adaptive_thresholding.py -i coins.png
import numpy as np
import argparse 
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# to remove high frequency edges we are not concerned with
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)


'''Having to manually select T is a pain, plus you might need more
than one T for different areas of the image.
Enter: adaptive thresholding.
    Considers neighbours of pixels, chooses optimal `T` for that region.    
'''

'''`ADAPTIVE_THRESH_MEAN_C` means we treat the mean of the neighbourhood as the `T`
11 : `neighbourhood size`telling it to examine a 11x11 neighbourhood
4 : `C`, a value subtracted from the mean. It's for us to fine tune
'''
t_img = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean thresh", t_img)
'''`ADAPTIVE_THRESH_GAUSSIAN_C` uses weighted mean to calculate `T`'''
t_img = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian thresh", t_img)

'''tweak neighbourhood size and C for your own purposes/experiments'''

cv2.waitKey(0)
