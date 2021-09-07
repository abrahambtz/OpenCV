import numpy as np
import cv2
def run():
    img = cv2.imread('img/python.png', cv2.IMREAD_GRAYSCALE) # Exiten 3 formas de abrir imagen; color, escala de grises o sin cambios
    # Mostramos la imagen
    cv2.imshow('Imagen', img) 
    # Guardamos la imagen.
    #cv2.imwrite('python_en_gris.png', img)
    # Espera la tecla 0
    cv2.waitKey(0) & 0xFF 
    cv2.destroyAllWindows(img) 
    # Si se cierra una ventana se especifica como parametro en caso contrario se cierran todas las ventanas


if __name__ == '__main__':
    run()