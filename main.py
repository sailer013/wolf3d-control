import numpy as np
import cv2
from mss import mss

WIDTH = 1028
HEIGHT = 672

bounding_box = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
