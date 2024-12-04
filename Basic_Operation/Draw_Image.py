import cv2
import numpy as np
img_path = r"D:/OpenCv/Resources/Whiteboard.png"
img=cv2.imread(img_path)

#Draw line
Line=cv2.line(img , (200,300),(500,600),(0,255,255),8)
cv2.imshow('Draw line',Line)
#cv2.imshow('Image_erode',img)
cv2.waitKey()