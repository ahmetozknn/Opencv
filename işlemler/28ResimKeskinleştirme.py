import cv2 
import numpy as np

img=cv2.imread("1.png")

s=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.float32)

sp=cv2.filter2D(img,cv2.CV_32F,s)


cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()