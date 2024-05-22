import cv2
import numpy as np

canvas=np.zeros((600,600,3),np.uint8)+255
f1=cv2.FONT_HERSHEY_PLAIN
f2=cv2.FONT_ITALIC
f3=cv2.FONT_HERSHEY_TRIPLEX

cv2.putText(canvas,"MERHABA",(25,95),f2,3,(255,0,0),cv2.LINE_AA)

#PUTTEXT İLE OLUR HERSEY ÖNCE PENCERE SONRA YAZI SONRA KORDİNAT SONRA FONT SONRA BÜYÜKLÜK SONRA RENK SONRA LİNE_AA

cv2.imshow("pencere",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
