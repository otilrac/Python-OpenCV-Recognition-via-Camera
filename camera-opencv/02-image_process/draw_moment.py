
import cv2
import sys
import numpy as np

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("moment.jpg")

# convert RGB to Gray to Binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(_, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# find contours
(contours, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cnt = contours[0]

((x, y), radius) = cv2.minEnclosingCircle(cnt)
M = cv2.moments(cnt)
center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
cv2.circle(image, center, 5, (0, 0, 255), -1)
cv2.imshow("Enclosing", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

