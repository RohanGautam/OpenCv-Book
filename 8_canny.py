# Run : python 8_cannt.py -i coins.png
import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

'''
In the before methods, edges are noisy.
Canny edge detector aims to make edges less noisy and crisp
It's a multi-step process:
1.Blur image to remove noise
2. sobel gradient in x,y direction
3.supress edges
4. hysterises thresholding stage -> if a pixel is edge-like or nah
'''

image = cv2.GaussianBlur(image, (5,5), 0)

'''
We provide 2 params: threshold 1 and threshold 2
`threshold 1` : gradient value below this, then not an edge
`threshold 2` : gradient value above this, then is an edge
gradient value between them: edge/not edge based on how their intensiies are connected
'''
canny = cv2.Canny(image,30,150)

# damn, those really are some crispy edges
cv2.imshow("Canny", canny)

cv2.waitKey(0)