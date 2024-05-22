import cv2
import numpy as np
src=cv2.imread("1.png")
def add_salt_pepper_noise(image):
    h,w=image.shape[:2]
    nums=100000 
    rows=np.random.randint(0,h,nums, dtype=np.uint)
    cols=np.random.randint(0,w,nums, dtype=np.uint)
    for i in range(nums):
        if i%2==1:
            image[rows[i],cols[i]]=(255,255,255)
        else:
            image[rows[i],cols[i]]=(0,0,0)
    return image

h,w=src.shape[:2]
copy=np.copy(src)

copy=add_salt_pepper_noise(copy)


cv2.imshow("1",src)
cv2.imshow("2",copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
