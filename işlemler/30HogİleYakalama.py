import cv2
import numpy as np

img = cv2.imread("2 (68).jpg")

# Görüntüyü yeniden boyutlandır
height, width, _ = img.shape
new_height = 600  # İstediğiniz yeni yükseklik
new_width = int((new_height / height) * width)
img_resized = cv2.resize(img, (new_width, new_height))

# HOG dedektörü
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# HOG dedektörü ile nesne tespiti
rects, weights = hog.detectMultiScale(img_resized, winStride=(4, 4), padding=(8, 8), scale=1.25)

# Tespit edilen nesneleri çiz
for x, y, w, h in rects:
    cv2.rectangle(img_resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Sonucu göster
cv2.imshow("Nesne Tespiti", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
