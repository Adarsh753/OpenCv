#In this part I  have practiced how  to resize an image and how to Crop an image

import cv2

#resize the image 

img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)
resz = cv2.resize(img ,(200,200))
print(img.shape)
cv2.imshow('Bird',img)
cv2.imshow('Resize_image',resz)
cv2.waitKey(0)

#Crop the image
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)
img_crp = img[200:300,300:400]
print(img.shape)
cv2.imshow('Bird',img)
cv2.imshow('crop_image',img_crp)
cv2.waitKey(0)