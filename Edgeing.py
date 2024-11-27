import cv2
import numpy as np
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)
img_edge =cv2.Canny(img,500,700)
img_dilate=cv2.dilate(img,np.ones((50, 50), dtype=np.int8))
img_erode= cv2.erode(img,np.ones((50, 50), dtype=np.int8))
cv2.imshow('Image_Edge',img)
cv2.imshow('Image_dila',img)
cv2.imshow('Image_erode',img)
cv2.waitKey()