# Run : python 5_histograms.py -i pupper.jpg
from matplotlib import pyplot as plt
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())  # this is  dictionary!
# load the image
image = cv2.imread(args["image"])  # returns a numpy array with image data
cv2.imshow("Original", image)
# make the image gray
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
''' calcHist(images, channels, mask, histSize, ranges)
`images` : a list of images to calculate histogram for
`channels` : channels you want to see hist for. [0] for gray, cuz only one channel. [0,1,2] if b,g,r channels for rgb
`mask` : calc histogram for region determined by the mask. `None` if for whole img
`histSize` : no. of bins for each channel. Eg: [32,32,32] if 32 bins for all 3 channels
`ranges` : The range of possible pixel values. Normally, this is [ 0, 256 ] for each channel, if you're using RGB
'''
hist = cv2.calcHist([grayImage], [0], None, [256], [0,256])
# make a figure
# plt.figure()
# # set title,x,y labels
# plt.title("Greyscale histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# # plot it
# plt.plot(hist)

# plt.xlim([0, 256])
'''Color!'''
# chans = cv2.split(image)
# colors = ("b", "g", "r")
# plt.figure()
# plt.title("’Flattened’ Color Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# for (chan, color) in zip(chans, colors):
#     hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
#     plt.plot(hist, color = color)
#     plt.xlim([0, 256])

# cv2.waitKey(0)
# plt.show()

'''Multi-dimensional histograms
for example - a 2d jointplot for red and blue channels. shows how both red and blue are TOGETHER distributed.
'''
chans = cv2.split(image)

fig = plt.figure()
ax = fig.add_subplot(131)
# using 32 bins below
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

cv2.waitKey(0)
plt.show()