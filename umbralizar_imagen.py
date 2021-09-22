import cv2
import numpy as np


def run():
    img = cv2.imread('img/input_image.jpg', cv2.IMREAD_GRAYSCALE)

    _, thresh1 = cv2.threshold(img, 3, 255, cv2.THRESH_BINARY) 
    _, thresh2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    _, thresh3 = cv2.threshold(img, 60, 255, cv2.THRESH_TRUNC)
    _, thresh4 = cv2.threshold(img, 60, 255, cv2.THRESH_TOZERO)
    _, thresh5 = cv2.threshold(img, 60, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Original', img)
    cv2.imshow('THRESH_BINARY', thresh1)
    cv2.imshow('THRESH_BINARY_INV', thresh2)
    cv2.imshow('THRESH_TRUNC', thresh3)
    cv2.imshow('THRESH_TOZERO', thresh4)
    cv2.imshow('THRESH_TOZERO_INV', thresh5)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    run()
