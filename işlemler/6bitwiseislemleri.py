import cv2
import numpy as np 

img1=cv2.imread("2 (65).jpg")
img2=cv2.imread("2 (68).jpg")
bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_xor=cv2.bitwise_xor(img1,img2)
bit_not1=cv2.bitwise_not(img2,img1)
bit_not2=cv2.bitwise_not(img1,img2)



cv2.imshow("1",img1)
cv2.imshow("2",img2)
cv2.imshow("and",bit_and)
cv2.imshow("or",bit_or)
cv2.imshow("xor",bit_xor)
cv2.imshow("not1",bit_not1)
cv2.imshow("not2",bit_not2)



cv2.waitKey(0)
cv2.destroyAllWindows()