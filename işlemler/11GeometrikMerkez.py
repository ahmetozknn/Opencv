import cv2 
import numpy as np
img=cv2.imread("us.png")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

l,thresh=cv2.threshold(gri,100,200,cv2.THRESH_BINARY)
m=cv2.moments(thresh)#moments agırlık merkezidir
print(m)
x=int(m["m10"]/m["m00"])
y=int(m["m01"]/m["m00"])

cv2.circle(img,(x,y),10,(255,0,0),-1)


cv2.imshow("2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()