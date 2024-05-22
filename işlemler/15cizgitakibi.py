import cv2
import numpy as np

img=cv2.imread("k.jpeg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kenar=cv2.Canny(gri,50,150)
cizgiler=cv2.HoughLinesP(kenar,1,np.pi/80,20)
print(cizgiler)

for i in cizgiler:
    x1,y1,x2,y2=i[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)





img=cv2.resize(img,(600,400),3)
cv2.imshow("s",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
