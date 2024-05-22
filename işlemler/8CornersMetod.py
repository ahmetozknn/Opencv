import cv2
import numpy as np 

img=cv2.imread("22.png")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gri=np.float32(gri)
corner=cv2.goodFeaturesToTrack(gri,30,0.01,20)
#ilk olarak değişken sonra max kaç köşe yakalasın sonra
#kalite değeri sonra en az kaç pixel olsun aralarında 
#değişkeni floata çevirmek lazım kardeş
#sonra inte çevirmek lazım
corner=np.int0(corner)

for c in corner:
    x,y=c.ravel()#düzleştirme metodudur
    cv2.circle(img,(x,y),3,(255,0,0),-1)



cv2.namedWindow("pencere",cv2.WINDOW_NORMAL)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()