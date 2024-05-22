import cv2
import numpy as np


img1=cv2.imread("2 (68).jpg",0)


sat,sut=img1.shape


m=cv2.getRotationMatrix2D((sut/2,sat/2),270,1)#getRotationmatrix2d unutma
d=cv2.warpAffine(img1,m,(sut,sat))#warpaffine unutma

cv2.imshow("1",d)
cv2.waitKey(0)
cv2.destroyAllWindows()