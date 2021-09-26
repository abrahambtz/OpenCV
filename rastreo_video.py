import numpy as np
import cv2
def run():
    cap = cv2.VideoCapture('rtsp://admins:abroot@192.168.0.2:554/stream1')
    while True:
        # Leer cada cuadro
        _, frame = cap.read()
        if _ == True:
            
            # Convertir BGR a HVS
            hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])
            #lower_red = np.array([20, 100, 100])
            #upper_red =  np.array([40, 255, 255])
           
            cv2.boundingRect

            mask = cv2.inRange(hvs, lower_blue, upper_blue)
            res = cv2.bitwise_and(frame, frame, mask=mask)

            resize = cv2.resize(frame, (1230, 650))
            cv2.imshow('Original', resize)
            resize = cv2.resize(mask, (1230, 650))
            cv2.imshow('Mask', resize)
            resize = cv2.resize(res, (1230, 650))
            cv2.imshow('RES', resize)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1) & 0xFF
if __name__ == '__main__':
    run()
