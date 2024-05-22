import cv2

cap=cv2.VideoCapture("2 (7).mp4")
vucut=cv2.CascadeClassifier("fulbody2.xml")

while True:
    ret,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies=vucut.detectMultiScale(gri,2.2,2)

    for x,y,w,h in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("1",frame)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()