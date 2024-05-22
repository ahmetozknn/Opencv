import cv2

# Kamera için VideoCapture objesi oluştur
cap = cv2.VideoCapture(0)

# Yüz tespiti için sınıflandırıcıyı yükle
yuz_casc = cv2.CascadeClassifier("frontalface.xml")

while True:
    # Kameradan bir frame al
    ret, frame = cap.read()
    
    # Eğer frame alınamazsa döngüden çık
    if not ret:
        break
    
    frame=cv2.flip(frame,1)
    # Gri tonlamaya dönüştür
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = yuz_casc.detectMultiScale(gri,1.1,4)

    # Tespit edilen yüzleri dikdörtgenlerle çevrele
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Frame'i ekranda göster
    cv2.imshow("Yüz Tespiti", frame)

    # q tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Kamera kaynağını serbest bırak
cap.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()
