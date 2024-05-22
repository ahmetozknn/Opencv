import cv2
import numpy as np
import pickle

try: 
    with open("kutu.pkl", "rb") as f:
        liste = pickle.load(f)
except FileNotFoundError:
    liste = []

def rotate_rectangle(rect, angle, center):
   
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
  
    rotated_rect = cv2.transform(np.array([rect]), rotation_matrix)[0]
    return rotated_rect

def mouse(event, x, y, flags, param):
    global liste
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
         x = x - 24 if x >= 24 else 0
         y = y - 14 if y >= 14 else 0
         liste.append((x, y))
        

    if event == cv2.EVENT_RBUTTONDBLCLK:
        for i, pos in enumerate(liste):
            x1, y1 = pos
            if x1 < x < x1+68 and y1 < y < y1+28:
                liste.pop(i)
    
    with open("kutu.pkl", "wb") as f:
        pickle.dump(liste, f)

while True:
    img = cv2.imread("B.jpg")
    for l in liste:
        x, y = l 
        rect = ((x, y), (x+68, y), (x+68, y+28), (x, y+28))
        rotated_rect = rotate_rectangle(rect, 90, (x+34, y+14))
   
        cv2.polylines(img, [np.int32(rotated_rect)], isClosed=True, color=(0, 0, 255), thickness=2)

    cv2.imshow("sekme", img)
    cv2.setMouseCallback("sekme", mouse)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
