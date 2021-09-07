# Abraham Baltazar García Moreno 🐍
# Importar librerias.
import numpy as np
import cv2

# Funcion sin ningun proceso.


def nothing():
    pass
# Funcion principal


def run():
    # Proceso: Definimos las imagenes que se pretende mostrar.
    img_0 = cv2.imread('img/python_value_0.png', cv2.IMREAD_UNCHANGED)
    img_1 = cv2.imread('img/python.png', cv2.IMREAD_UNCHANGED)
    img_2 = cv2.imread('img/python_value_2.png', cv2.IMREAD_UNCHANGED)
    # Proceso: Mensaje de Trackbar
    opt = 'Valor 0,1,2: '
    # Proceso: Nombramos nuestra ventada para proyectar nuestras imagens
    cv2.namedWindow('Imagenes')
    # Proceso: Creamos nuestras TrackBar con 3 opciones 0, 1, 2.
    cv2.createTrackbar(opt, 'Imagenes', 0, 2, nothing)
    # Proceso: Declaramos nuestra variable global la cual se estara intercalando dentro del while
    img = img_0
    # Proceso: While infinito hasta esperar la tecla ESC
    while(1):
        # Mostramos nuestra imagen inicial en este caso img_0
        cv2.imshow('Imagenes', img)
        # KEY sera igual al valor en decimal de la tecla que se espera presionar mientras corremos nuestro programa
        key = cv2.waitKey(1)
        # Si KEY es igual a 27, en este caso ESC en decimal es 27, esto finalizara el ciclo lo cual termina el programa.
        if key == 27:
            break
        # Obtenemos el valor de el TrackBar.
        valueTrackbar = cv2.getTrackbarPos(opt, 'Imagenes')
        # De acuerdo al menu de opciones es que se muestra la imagen
        if valueTrackbar == 0:
            img = img_0
        elif valueTrackbar == 1:
            img = img_1
        elif valueTrackbar == 2:
            img = img_2


if __name__ == '__main__':
    run()
