import os

import cv2

BASE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(BASE_DIR)
ASSESTS_PATH = os.path.join(ROOT, 'assets')

img = cv2.imread(os.path.join(ASSESTS_PATH, 'test.png'))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

cv2.imshow('Frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()