# Thresolding of the image
import cv2
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)
print(img.shape)
img_cnvrt_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold(img_cnvrt_g,80,255,cv2.THRESH_BINARY)
thresh = cv2.blur(thresh,(10,10))
ret , thresh = cv2.threshold(thresh,50,255,cv2.THRESH_BINARY)
#ret , thresh = cv2.adaptiveThresholdthreshold(img_cnvrt_g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.ADAPTIVE_THRESH_MEAN_C,255.24)
cv2.imshow('Image_Blur_m',thresh)
cv2.imshow('Image',img_cnvrt_g)
cv2.waitKey(4000)
