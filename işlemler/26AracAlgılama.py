import cv2

img=cv2.imread("car.jpg")
araba=cv2.CascadeClassifier("car.xml")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

car=araba.detectMultiScale(gri,1.08,2)

for x,y,w,h in car:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("1",img)

cv2.waitKey(0)
cv2.destroyAllWindows()