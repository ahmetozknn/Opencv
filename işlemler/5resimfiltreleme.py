import cv2
import numpy as np

img1=cv2.imread("a.jpg")
img2=cv2.imread("2 (65).jpg")
img3=cv2.imread("2 (68).jpg")
img1=cv2.resize(img1,(400,400))


#blr=cv2.blur(img1,(10,10)) #cv2.blur önce hangi resminde yapcagın sonra ne kadar blur atcagın
#gb=cv2.GaussianBlur(img1,(11,11),cv2.BORDER_DEFAULT)#sadece tek sayılar alır
mb=cv2.medianBlur(img1,11)#tek sayılar olması lazım
b=cv2.bilateralFilter(img1,9,25,25)# aradaki blur giderilir
cv2.imshow("orj",img1)
cv2.imshow("mb",mb)
cv2.imshow("mbw",b)




#cv2.imshow("blur",blr)
#cv2.imshow("g",gb)
cv2.waitKey(0)
cv2.destroyAllWindows()