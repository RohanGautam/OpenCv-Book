# Run : python 8_sobel_and_laplacian.py -i coins.png
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
Gradients and edge detection -> points where pixel intensities change distinctly
'''
'''
we use float for output as uint8 doesnt capture negative values,
which might be present if we get negative slopes(transition from white->black)
Laplacian[differential operator]: a large Laplacian at a point reflects a “nonconformist” (i.e., different from average) character for the function there
'''
lap = cv2.Laplacian(image, cv2.CV_64F) # second is arg for dtype of output image
lap = np.uint8(np.abs(lap)) # take abs value, convert back to uint8. if not, you'll miss edges!
cv2.imshow("Laplacian", lap)


'''using the sobel gradient representation'''
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) # to find vertical edges
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) # to find horizontal edges
# we then ensure we find all edges by
# taking the absolute value of the floating point image and
# then converting it to an 8-bit unsigned integer
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# combine both to find gradient images in both x and y directions
combined = cv2.bitwise_or(sobelX, sobelY)

# cv2.imshow("Sobel X", sobelX)
# cv2.imshow("Sobel Y", sobelY)

# "noisy" edges doeeeee
cv2.imshow("Sobel Combined", combined)

cv2.waitKey(0)