import cv2
import numpy as np

img = cv2.imread("4.png")

def harris(image):
    blockSize = 2
    apertureSize = 3
    k = 0.04
    threshold_value = 120
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, blockSize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype=np.uint8)
    cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > threshold_value:
                cv2.circle(image, (j, i), 2, (0, 255, 0), 2)

    return image

result = harris(img)
cv2.imshow("Köşe Tespiti", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
