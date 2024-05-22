import cv2
import numpy as np
img=cv2.imread("a.jpg")
renk=img[100,300]
mavi=img.item(150,150,0)
print(mavi)
img.itemset((150,150,0),200)
img[200,300,0]=0
print(img[200,300])
print("mavi ",mavi)
print(renk)#o kordinattaki renklerini verir
print(img.shape)#boyutlarını verir
cv2.imshow("pencere",img)

cv2.waitKey(0)
cv2.destroyAllWindows()