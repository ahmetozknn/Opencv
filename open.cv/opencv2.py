import cv2
img=cv2.imread("a.jpg",cv2.IMREAD_GRAYSCALE) #imread görüntünün konumu okur IMREAD GRAY SCALE GRİ TONLARINA ÇEVİRİR
img=cv2.resize(img,(1600,400)) #sizenı belirtir 
cv2.namedWindow("image",cv2.WINDOW_NORMAL) # GÖRÜNTÜYÜ BÜYÜTME KÜÇÜTMEYİ AÇAR
cv2.imshow("image",img) #imshow görüntüyü açar
cv2.imwrite("copy.jpg",img)

cv2.waitKey(0) #waitkey 0 görüntüyü tam olarak açar


cv2.destroyWindow() #acık olan tüm sekmeleri kapar