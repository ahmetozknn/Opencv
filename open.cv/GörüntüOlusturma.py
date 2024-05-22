import cv2
import numpy as np



img=np.zeros((20,20,3),np.uint8)+255

img[0,0]=200
img[0,1]=180
img[0,2]=150
img[0,3]=100
img[0,4]=50
img[0,5]=0
img=cv2.resize(img,(300,300),interpolation=cv2.INTER_AREA) #interpolation=cv2.INTER_AREA bu görüntüyü değiştirirken hataların önüne geçer






print(img)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()