import cv2
import numpy as np
import pickle

capture = cv2.VideoCapture("video2.mp4")


def check(frames):
   
    spacecounter=0
    for pos in liste:
        x, y = pos
        crop = frames[y:y+28, x:x+48]
        count = cv2.countNonZero(crop)
        print("count", count)
        if count < 150:
            color = (255, 0, 0)
            spacecounter+=1
        else:
            color = (0, 0, 255)  
        cv2.rectangle(frame, (x, y), (x+28, y+68), color, 2)
                      
    cv2.putText(frame,f"bos: {spacecounter} /{len(liste)}",(15,35),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    for pos in liste:
        x, y = pos
        center = (x + 24, y + 14)  
        angle = 90  
        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        döndürmeişlemi = cv2.warpAffine(frame, matrix, (48, 28))
        cv2.imshow("döndürme işlemi", döndürmeişlemi)
      


with open("kutu.pkl", "rb") as f:
    liste = pickle.load(f)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Video bitti veya açılamadı.")
        break
    

    frame = cv2.resize(frame, (1270, 727))
    
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (3, 3), 1)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    median = cv2.medianBlur(thresh, 5)
    dilates = cv2.dilate(median, np.ones((3, 3)), iterations=2)
   
    check(dilates)
    cv2.imshow("sekme", frame)
    
    if cv2.waitKey(200) & 0xFF == ord("a"):
        break

capture.release()
cv2.destroyAllWindows()
