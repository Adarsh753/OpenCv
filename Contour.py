import cv2
img_path = r"D:\OpenCv\Resources\BB.jpg"
img=cv2.imread(img_path)

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_grey, 127 , 255, cv2.THRESH_BINARY_INV)

contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('Img',img)
cv2.imshow('Img_gry',img_grey)
cv2.imshow('Img_cont',thresh)
cv2.waitKey(0)
