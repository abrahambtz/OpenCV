import numpy as np
import cv2

def run():
    img = cv2.imread("img/Messi.jpg")
    head = img[75:135, 205:265]
    

    cv2.imshow("Imagen", head)
    cv2.imwrite('img/head_messi.jpg', head)
    cv2.waitKey(0) & 0xFF
    cv2.destroyWindow("Imagen")


if __name__ == "__main__":
    run()