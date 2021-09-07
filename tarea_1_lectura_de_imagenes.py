# Abraham Baltazar García Moreno 🐍
import numpy as np
import cv2

# Funcion: Creamos una función para abrir imágenes,
# indicando el nombre de la ventana, el nombre del
# archivo y el tipo de lectura.


def open_image(window_name, file_name, type_reading):
    rute = 'img/python.png'
    img = cv2.imread(rute, type_reading)
    cv2.imshow(window_name, img)
    cv2.imwrite(file_name, img)


def run():
    # Proceso: Invocamos a la funcion open_image para abrir las 3 imagenes.
    open_image('Imagen sin cambios',
               'img/python_IMREAD_UNCHANGED.png', cv2.IMREAD_UNCHANGED)
    open_image('Imagen escala de grises',
               'img/python_IMREAD_GRAYSCALE.png', cv2.IMREAD_GRAYSCALE)
    open_image('Imagen de color',
               'img/python_IMREAD_COLOR.png', cv2.IMREAD_COLOR)
    # Proceso: Esperamos una tecla para finalizar el programa.

    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
