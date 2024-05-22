import cv2
import numpy as np 

img1=cv2.imread("2.png")
img2=cv2.imread("22.png")

fark=cv2.subtract(img1,img2)

cv2.imshow("1",fark)
cv2.imshow("2",img1)
cv2.imshow("3",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()