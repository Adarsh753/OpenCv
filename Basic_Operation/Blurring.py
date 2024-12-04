#Blurring the image by defining shape and size and amount of image to be blured
import cv2
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)
print(img.shape)
img_blr = cv2.blur(img ,(10,10))
img_blr_Gussian_blr = cv2.GaussianBlur(img , (7,5) , 2)
img_blr_med_blr = cv2.medianBlur(img ,9)
cv2.imshow('Image_Blur',img_blr)
cv2.imshow('Image_Blur_g',img_blr_Gussian_blr)
cv2.imshow('Image_Blur_m',img_blr_med_blr)
cv2.waitKey(4000)
