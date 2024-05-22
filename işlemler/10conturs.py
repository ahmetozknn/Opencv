import cv2
import numpy as np 

img=cv2.imread("22.png")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thres=cv2.threshold(gri,100,200,cv2.THRESH_BINARY)
cont,a=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contourları bulur
#print(cont)

cv2.drawContours(img,cont,-1,(255,0,0),2) #köşe kenar çizgilerini çizer


cv2.imshow("2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()