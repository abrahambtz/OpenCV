import numpy as np
import cv2

def run():
    # Crear imagen en negro.
    img = np.zeros((512,512, 3), np.uint8)
    # Dibujando una linea diagonal azul con una anchura de 5px
    img = cv2.line(img, (0,0), (512,512), (255, 0, 0), 5)
    img = cv2.rectangle(img, (250,0), (450, 300), (0,255,0), 5)
    img = cv2.circle(img, (250,250), 50 ,(0,0, 255), -10)
    img = cv2.ellipse(img, (300,250), (100, 50), 90, 50, 180, 255, 5)

    pts = np.array([[30, 35],[40,50],[50, 35],[90, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 20, 100), 3)

    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img, 'OpenCV', (10,400), font, 5, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow('Imagen en negro', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    run()