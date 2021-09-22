import numpy as np
import cv2
def run():
    #cap = cv2.VideoCapture(0)
    #fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    
    cap = cv2.VideoCapture('rtsp://admins:abroot@192.168.0.2:554/stream1')
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
   
    out = cv2.VideoWriter('video/video.avi', fourcc, 20.0, (1920,1080))
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == True:
            resize = cv2.resize(frame, (1230, 650)) 
            out.write(frame)
            cv2.imshow('frame',resize)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1) & 0xFF

if __name__ == '__main__':
    run()