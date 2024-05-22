import cv2

cap=cv2.VideoCapture(0)
yuz=cv2.CascadeClassifier("frontalface.xml")
eyes=cv2.CascadeClassifier("eye.xml")

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=yuz.detectMultiScale(gri,1.2,4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    gri1 = gri[y:y+h, x:x+w]
    img2 = frame[y:y+h, x:x+w]

    eyes1 = eyes.detectMultiScale(gri1)

    for ex, ey, ew, eh in eyes1:
        cv2.rectangle(img2, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

    cv2.imshow("1",frame)
    if not ret:
        break

    if cv2.waitKey(20)& 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()