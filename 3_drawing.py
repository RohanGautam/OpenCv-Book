import numpy as np
import cv2

# defining our own canvas with numpy arrays!
canvas = np.zeros((300, 300, 3), dtype="uint8") # (0,0,0) is black
cv2.imshow("Canvas", canvas)

'''drawing lines'''
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3) # last one is thickness - 3 pixels
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

'''drawing rectangles'''
cv2.rectangle(canvas, (10,10), (60,60), green) # specify start and end of rect's diagonal 
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50,10), (250,60), red, -7) # negative value to have a filled in rectangle
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

'''drawing circles'''
canvas = np.zeros((300, 300, 3), dtype = "uint8") # refresh canvas
width, height, channels = canvas.shape
centerX, centerY = width//2, height//2

# cv2.circle(canvas, (centerX, centerY), 40, red)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# drawing a bullseye
for radius in range(20, 150, 30):
    cv2.circle(canvas, (centerX, centerY), radius, red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#abstract art! Drawing 25 random circles
canvas = np.zeros((300, 300, 3), dtype = "uint8") # refresh canvas
for _ in range(25) :
    radius = np.random.randint(0, high = 200)
    color = np.random.randint(0, high = 255, size = 3).tolist()
    center = tuple(np.random.randint(0, 300, size = 2).tolist())
    cv2.circle(canvas, center, radius, color, -1) # negative thickness to fill
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
