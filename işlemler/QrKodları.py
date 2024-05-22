import cv2


path="/QrKodları/"
src=cv2.imread(path+"qr.png")
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
qrcoder=cv2.QRCodeDetector()

codeinfo,points,straight_qrcode=qrcoder.detectAndDecode(gray)

print(points)