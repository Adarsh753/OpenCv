#Convert rgb to bgr colour 
import cv2
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)
img_cnvrt = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_cnvrt_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_cnvrt_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('Bird',img)
cv2.imshow('CVT_image',img_cnvrt)
cv2.imshow('CVT_image_grey',img_cnvrt_g)
cv2.imshow('CVT_image_HSV',img_cnvrt_HSV)
cv2.waitKey(0)
