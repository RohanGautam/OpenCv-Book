# Run : python 6_blurring.py -i pupper.jpg
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())  # this is  dictionary!
# load the image
image = cv2.imread(args["image"])  # returns a numpy array with image data
# h,w = image.shape[:2]
# cv2.rectangle(image, (0,0),(7,h), (0,0,255), -1) # to see the effect of edge loss
cv2.imshow("Original", image)

'''
Blurring!
* Method 1 - averaging
    define a (k x k) sliding window[known as a conv. kernel] [k is odd], which slides
    left-right&top-down[everywhere], and the pixel at the center 
    of this window will be the avg of all the other pixels in the window

'''

# let's stack 3 images with different values of k and compare em
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7)),
])
cv2.imshow("Averaged w averaging", blurred)

''' 
* Method 2 - Gaussian blur
    the pixel at the center of this window will be the
    *weighted *avg of all the other pixels in the window
    (more weight if pixel closer to pixel at center of the kernel).
    Looks more "natural"
'''
blurred = np.hstack([
    # last param is sigmaX. If zero, opencv automatically calculates it based on kernel size
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0),
])
cv2.imshow("Averaged w Gaussian blur", blurred)
'''
Method 3 : median blur:
    >Replace central pixel with the *median* of the neighbourhood
    >Effective at removing salt-and-pepper noise from image.
    >Different from avg and gaussian as the selected pixel *will*
    exist in the neighbourhood. [may not exist if you're taking a plain average]
    >Doesn't look like a "motion" blur,, just removes a layer of detail and noise
'''
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)])
cv2.imshow("Median blur", blurred)


'''
Uptil now, since we are using kernels of size (k,k),
we lose edges of the image[of k pixels all round], because the center
of the square only begins k pixels in.
The method below maintains edges.
Method 4: bilateral blurring:
    > uses 2 normal/gaussian distributions
    > a square kernel not used. Instead, the size and number of neighbours
    is determined by one of the normal distributions
    > the second normal dist models pixel intensity, much like in gaussian blur.
    > Drawback: it's slow compared to ones above.
.
'''

# In the first filter, 5 is diameter of pixel neighbourhood.
# 21 is colorSigma. large = more colors while calc blur
# the next 21 is SpaceSigma. Large = further pixels can influence blur(if similar color)
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("Bilateral", blurred)


cv2.waitKey(0)
