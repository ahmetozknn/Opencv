import cv2
import numpy as np
img=cv2.imread("2.png")
img=cv2.resize(img,(600,600))
roi=img[40:130,100:250]# ilk kısım x 2. kısım y

cv2.namedWindow("roi",cv2.WINDOW_NORMAL)

cv2.imshow("roi",roi)

cv2.imshow("pencere",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

