import numpy as np
import cv2


def run():
    
    b = input('B: 0-255: ')
    g = input('G: 0-255: ')
    r = input('R: 0-255: ')
    colorBGR = np.uint8([[[b, g, r]]])
    colorHVS = cv2.cvtColor(colorBGR, cv2.COLOR_BGR2HSV)
    print(colorHVS)

if __name__ == '__main__':
    run()
