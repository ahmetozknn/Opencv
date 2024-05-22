import cv2


img=cv2.imread("8.jpeg")

yuz=cv2.CascadeClassifier("frontalface.xml")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#caascade ile dosyayı ekliyoruz
#detectMultiScale ile fonksiyonu cagırıyoz
faces=yuz.detectMultiScale(gri,1.3,4)


for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()