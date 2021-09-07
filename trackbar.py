import numpy as np
import cv2

def nada():
    pass

def run():
    # Crear imagen en negro
    img = np.zeros((300, 700, 3), np.uint8)
    cv2.namedWindow('Imagen')

    # Crear barra de dezplazamiento para colores.
    cv2.createTrackbar('R', 'Imagen', 0, 255, nada)
    cv2.createTrackbar('G', 'Imagen', 0, 255, nada)
    cv2.createTrackbar('B', 'Imagen', 0, 255, nada)

    # Crear barra como interruptor.
    switch = ' 0 : Apagado \n 1 : Encendido.'
    cv2.createTrackbar(switch, 'Imagen', 0, 1, nada)

    while(1):   
        cv2.imshow('Imagen', img)
        k = cv2.waitKey(1)
        
        if k == 27:
            break
           
        # Obtener posicion de las cuatro barras
        r = cv2.getTrackbarPos('R', 'Imagen')
        g = cv2.getTrackbarPos('G', 'Imagen')
        b = cv2.getTrackbarPos('B', 'Imagen')
        s = cv2.getTrackbarPos(switch, 'Imagen')
        
        if s == 0:
            img[:] = 0
        else:
            img[:] = [r,g,b]

            
if __name__ == '__main__':
    run()