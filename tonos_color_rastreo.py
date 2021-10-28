import cv2
import numpy as np


def nothing():
    pass

def run():
    #cap = cv2.VideoCapture('rtsp://admins:abroot@192.168.0.2:554/stream1')
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Video')
    cv2.createTrackbar('R', 'Video', 0, 255, nothing)
    cv2.createTrackbar('G', 'Video', 0, 255, nothing)
    cv2.createTrackbar('B', 'Video', 0, 255, nothing)
    cv2.createTrackbar('C', 'Video', 0, 2, nothing)
    img = np.zeros((1,300, 3), np.uint8)
    while True:
        ret, frame = cap.read()
        if ret == True:            
            frame_hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            r = cv2.getTrackbarPos('R', 'Video')
            g = cv2.getTrackbarPos('G', 'Video')
            b = cv2.getTrackbarPos('B', 'Video')
            s = cv2.getTrackbarPos('C', 'Video')
            bgr_color = np.uint8([[[b, g, r]]]) 
            hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
            lowerLimit = hsv_color[0][0][0] - 10, 50, 50
            upperLimit = hsv_color[0][0][0] + 10, 255, 255
            if lowerLimit[0] < 0:
                if r > 240 and g > 240 and b > 240:
                    lower_color = np.array([0, 0, 50])
                    upper_color = np.array([0, 0, 255])
                if r < 10 and g < 10 and b < 10:
                    lower_color = np.array([0, 0, 0])
                    upper_color = np.array([0, 0, 0])
            else:
                lower_color = np.array([lowerLimit[0],lowerLimit[1], lowerLimit[2]])
                upper_color = np.array([upperLimit[0], upperLimit[1], upperLimit[2]])


            cv2.boundingRect
            mask = cv2.inRange(frame_hvs, lower_color, upper_color)            
            res = cv2.bitwise_and(frame, frame, mask=mask)


            if s == 0:
                img = cv2.resize(frame, (1030, 450))
            elif s == 1:
                img = cv2.resize(res, (1030, 450))
            elif s == 2:
                img = cv2.resize(mask, (1030, 450))
            cv2.imshow('Video', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1) & 0xFF

if __name__ == '__main__':
    run()

    