
import cv2
import sys
import numpy as np

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("lena512rgb.png")

# convert RGB to Gray to Binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(_, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", binary)
cv2.waitKey(0)

kernel = np.ones((3,3), np.uint8)
erode  = cv2.erode(binary, kernel, iterations=1)
cv2.imshow("Erode", erode)
print "Erode image..."
cv2.waitKey(0)

dilate = cv2.dilate(binary, kernel, iterations=1)
cv2.imshow("Dilate", dilate)
print "Dilate image..."
cv2.waitKey(0)

cv2.destroyAllWindows()


