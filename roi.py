import numpy as np
import cv2

def run():
    img = cv2.imread("img/Messi.jpg")
    balon = img[75:135, 205:265]
    
    img[273:333, 100:160] = balon

    cv2.imshow("Imagen", img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyWindow("Imagen")


if __name__ == "__main__":
    run()