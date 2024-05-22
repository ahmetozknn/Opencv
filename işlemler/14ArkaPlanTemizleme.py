import cv2
import numpy as np 
cap=cv2.VideoCapture("3.mp4")
sub=cv2.createBackgroundSubtractorMOG2(history=200,varThreshold=1000,detectShadows=True)
while True:
    ret,frame=cap.read()
    m=sub.apply(frame)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break
    
    cv2.imshow("frame",frame)
    cv2.imshow("m",m)


cap.release()
cv2.destroyAllWindows()