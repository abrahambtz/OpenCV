import numpy as np
import cv2
def run():
    cap = cv2.VideoCapture('video/video.avi')
   
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True: 
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1) & 0xFF

if __name__ == '__main__':
    run()