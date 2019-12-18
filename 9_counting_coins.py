# Run : python 9_counting_coins.py -i coins.png
import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# bigger kernel here->less noise
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Original", blurred)

'''Contour is a continuous curve (no gaps)'''
# gradient value below 30 : non edges, above 150: sure edges
canny = cv2.Canny(blurred,30,150)
cv2.imshow("Edges w canny", canny)

# RETR_EXTERNAL for only outermost contours
# last arg is how to approximate contour, as actually findng all pts is computationally wasteful
# cv2.CHAIN_APPROX_NONE if you want all points of contour to be calculates
# CHAIN_APPROX_SIMPLE approximates by compressing horiz,vert,diag into it's endpoints only

#returns image which it modifies (which is why we pass a deepcopy),
# the contours. We only take what we want.
contours, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f'I count {len(contours)} coins!')

coins = image.copy()
# -1 means draw "all" contours. we can give an index `i` instead to only draw that contour
# draw with color green
# thickness 2
cv2.drawContours(coins, contours, -1, (0,255,0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

for i,contour in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(contour)
    coin = image[y:y+h, x:x+w]
    cv2.imshow(f'coin {i+1}', coin)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    # `minEnclosingCircle` fits a circle to contour
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(contour)
    #draw circle to mask
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow(f'coin {i+1} with mask', cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)