import cv2
import numpy as np


def run():
    img = cv2.imread('img/input_image.jpg', cv2.IMREAD_GRAYSCALE)

    thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 2) 
    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) 

    cv2.imshow('Original', img)
    cv2.imshow('ADAPTIVE_THRESH_MEAN_C', thresh1)
    cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C', thresh2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    run()
