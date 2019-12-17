import numpy as np
import cv2


def translate(image, x, y):
    '''Translation : shifting the image along the x and y axes 
        `[[1, 0, x],  x : pixels to shift right(if +) or left (if -)`

         `[0, 1, y]]  y : pixels to shift down(if +) or up (if -) `
    '''
    # matrix(of floats-required) describing translation
    M = np.float32([[1, 0, x], [0, 1, y]])
    imgShape = (image.shape[1], image.shape[0])  # (w,h)
    # `warpAffine` applies the matrix transformation to the image
    return cv2.warpAffine(image, M, imgShape)


def rotate(image, theta, center=None, scale=1.0):
    ''' `theta` is the angle in degrees'''
    imgShape = (image.shape[1], image.shape[0])  # (w,h)
    if center is None:
        center = (image.shape[1]//2, image.shape[0]//2)
    M = cv2.getRotationMatrix2D(center, theta, scale)
    return cv2.warpAffine(image, M, imgShape)


def resize(image, width=None, height=None):
    dim = None
    if width is None and height is None:
        return image
    if width is not None:
        # given width/(width of original image)
        aspectRatio = width / image.shape[1]
        dim = (width, int(image.shape[0]*aspectRatio))
    elif height is not None:
        # given height/(height of original image)
        aspectRatio = height / image.shape[0]
        dim = (int(image.shape[1]*aspectRatio), height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

def flip(image, horizontally = False, vertically = False):
    if horizontally:
        image = cv2.flip(image, 1)
    if vertically:
        image = cv2.flip(image, 0) # if (-) value as flip code, will flip both ways directly
    return image