import cv2

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    kenar=cv2.Canny(frame,50,75)#daha hassas çalışması için az koy
    
    cv2.imshow("frame",frame)
    cv2.imshow("2",kenar)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()