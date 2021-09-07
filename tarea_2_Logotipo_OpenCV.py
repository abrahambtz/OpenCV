import numpy as np
import cv2
# Funcion: Crea las figuras circulares, los parametros son posicion, imagen, orientacion y color
def draw_shape(x, y, img, orientation, color):
    # Definimos la orientacion de la figura
    if orientation == 'up_up':
        pt1 = (256+x, 251-y)
        pt2 = (223+x, 201-y)
        pt3 = (288+x, 201-y)
    elif orientation == 'dow_dow':
        pt1 = (256+x, 261-y)
        pt2 = (225+x, 311-y)
        pt3 = (288+x, 311-y)
    elif orientation == 'up_right':
        pt1 = (261+x, 251-y)
        pt2 = (286+x, 207-y)
        pt3 = (311+x, 251-y)
    
    # Creamos dos circulos de dos tamaños y de color distinto
    img = cv2.circle(img, (256+x, 256-y), 50, color, -10)
    img = cv2.circle(img, (256+x, 256-y), 20, (255, 255, 255), -10)

    # Creamos arreglos de los vertices del triangulo
    triangle_cnt = np.array([pt1, pt2, pt3])
    # Dibujamos nuestro triangulo con los vertices.
    cv2.drawContours(img, [triangle_cnt], 0, (255, 255, 255), -1)
    return img

# Funcion: Inicio del programa.
def run():
    # Crear imagen en blanco.
    img = np.ones((512, 512, 3), np.uint8) * 255
    # Creamos nuestras figuras circulares
    img = draw_shape(-58, 0, img, 'up_right', (0, 255, 0))  # c1
    img = draw_shape(0, 100, img, 'dow_dow', (0, 0, 255))  # c2
    img = draw_shape(58, 0, img, 'up_up', (255, 0, 0))  # c3

    # Creamos nuestro texto.
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, 'OpenCV', (135, 350), font, 3, (0, 0, 0), 3, cv2.LINE_AA)
    # Mostramos nuestra imagen en la ventan
    cv2.imshow('Open CV', img)
    # Esperamos una tecla
    cv2.waitKey(0)
    # Liberamos la ventana
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run()
