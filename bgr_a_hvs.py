import numpy as np
import cv2


def run():
    colorBGR = np.uint8([[[255,0,0]]])
    colorHVS = cv2.cvtColor(colorBGR, cv2.COLOR_BGR2HSV)
    print(colorHVS)

if __name__ == '__main__':
    run()