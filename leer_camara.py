import numpy as np
import cv2

def run():
    cap = cv2.VideoCapture('rtsp://admins:abroot@192.168.0.2:554/stream1')
    while(True):
        # Capture cuadro por cuadro
        ret, frame = cap.read()
        resize = cv2.resize(frame, (1230, 650)) 
        # Operacion sobre el cuadro actual
        # gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', resize)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    
    cv2.destroyAllWindows()


    
if __name__ == "__main__":
    run()