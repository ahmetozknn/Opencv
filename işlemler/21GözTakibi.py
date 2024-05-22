import cv2

img = cv2.imread("9.jpeg")
yuz_casc = cv2.CascadeClassifier("frontalface.xml")
goz_casc = cv2.CascadeClassifier("eye.xml")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Yüzleri tespit et
faces = yuz_casc.detectMultiScale(gri, scaleFactor=1.2, minNeighbors=7)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Yüz bölgesini seç
    roi_gray = gri[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # Gözleri tespit et
    eyes = goz_casc.detectMultiScale(roi_gray)

    for ex, ey, ew, eh in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
