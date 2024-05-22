import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame=cap.read()
    cv2.namedWindow("webcam",cv2.WINDOW_NORMAL)#görüntü büyüttk küçülkttük
    frame=cv2.flip(frame,1) #ters çevirdik be oglum
    cv2.imshow("webcam",frame) #görüntüyü açtırdık
    if cv2.waitKey(1) & 0xFF==ord("q"):## q basınca kapatma tusu
        break

    cv2.waitKey(10)#saniyede kaç kare yakaladıgı az sayı olursa daha iyi

cap.release()
cv2.destroyAllWindows()