import cv2
import numpy as np
canvas=np.zeros((500,500,3),np.uint8)+255
#baslangıc=(320,500)
#cv2.line(canvas,baslangıc,(300,300),(80,40,188),thickness=5)
##önce hangi obje sonra başlangıç konumu sonra bitiş konumu 
##sonra rengi sonra kalınlığı yazcan
#cv2.line(canvas,(200,200),(400,400),(190,50,75),4)

#cv2.rectangle(canvas,(40,40),(300,300),(180,58,68),-1)

#cv2.circle(canvas,(100,100),100,(255,00,0),2)
u1=300,300
u2=300,200
u3=200,200
cv2.line(canvas,u1,u2,(0,0,0),2)
cv2.line(canvas,u2,u3,(0,0,0),2)
cv2.line(canvas,u3,u1,(0,0,0),2)

cv2.imshow("table",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
