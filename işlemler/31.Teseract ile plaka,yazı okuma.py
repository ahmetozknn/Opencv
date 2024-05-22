from PIL import Image
import pytesseract
import cv2
import numpy as np 
import imutils

#img=Image.open("M.png")
#text=pytesseract.image_to_string(img,lang="eng")
#print(text)

img=cv2.imread("a.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtre=cv2.bilateralFilter(gri,7,200,200)
kose=cv2.Canny(filtre,40,200)
kontur,a=cv2.findContours(kose,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=imutils.grab_contours((kontur,a))
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)[:10]

ekran=0

for i in cnt:
    eps=0.018*cv2.arcLength(i,True)
    aprx=cv2.approxPolyDP(i,eps,True)
    if len(aprx==4):
        ekran=aprx
        break
maske=np.zeros(gri.shape,np.uint8)
yenimaske=cv2.drawContours(maske,[ekran],0,(255,255,255),-1)
yazı=cv2.bitwise_and(img,img,mask=maske)

(x,y)=np.where(maske==255)
(ustx,usty)=(np.min(x),np.min(y))
(altx,alty)=(np.max(x),np.max(y))
kirp=gri[ustx:altx,usty:alty+1]



#cv2.imshow("1",gri)
#cv2.imshow("12",filtre)
#cv2.imshow("123",kose)
cv2.imshow("3",yenimaske)
cv2.imshow("4",yazı)
cv2.imshow("5",kirp)



cv2.waitKey(0)
cv2.destroyAllWindows()