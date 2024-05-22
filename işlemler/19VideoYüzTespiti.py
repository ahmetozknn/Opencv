import cv2
import numpy as np

cap = cv2.VideoCapture(0)
yuz = cv2.CascadeClassifier("frontalface.xml")

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    if not ret:
        break

    frame = cv2.resize(frame, (600, 600))

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = yuz.detectMultiScale(gri, 2, 3)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("1", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
