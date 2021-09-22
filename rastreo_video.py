import numpy as np
import cv2
def run():
    cap = cv2.VideoCapture('rtsp://admins:abroot@192.168.0.2:554/stream1')
    while(1):
        # Leer cada cuadro
        _, frame = cap.read()
        if _ == True:
            # Convertir BGR a HVS
            hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])
            mask = cv2.inRange(hvs, lower_blue, upper_blue)

            res = cv2.bitwise_and(frame, frame, mask=mask)
            resize = cv2.resize(frame, (1230, 650))
            resize = cv2.resize(mask, (1230, 650))
            resize = cv2.resize(res, (1230, 650))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1) & 0xFF
if __name__ == '__main__':
    run()
