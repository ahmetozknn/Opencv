import cv2
import numpy as np
# Load the pre-trained deep learning face detector model from OpenCV
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.xml", "res10_300x300_ssd_iter_140000.caffemodel")

cap = cv2.VideoCapture("video3.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video bitti veya açılamadı")
        break

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        # Confidence threshold
        if confidence < 0.5:
            continue

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    cv2.imshow("video", frame)

    if cv2.waitKey(100) & 0xFF == ord("a"):
        break

cap.release()
cv2.destroyAllWindows()
