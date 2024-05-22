import cv2
import numpy as np

img=cv2.imread("2 (65).jpg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img=cv2.resize(img,(600,600),3)
img1=cv2.resize(img1,(600,600),3)
img2=cv2.resize(img2,(600,600),3)
print(img.shape)
cv2.imshow("mezuniyet",img)
cv2.imshow("rgb",img1)
cv2.imshow("hsv",img2)
cv2.imshow("gray",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()