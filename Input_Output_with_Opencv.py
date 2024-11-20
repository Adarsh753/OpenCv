# This file is used to practice Input/Output of an image with OpenCV
import cv2

#read an image
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)

#write an image
img2=cv2.imwrite(r'D:/OpenCv/Resources/Bird_write.jpeg',img)

#visualize an image

cv2.imshow('Bird',img)
cv2.waitKey(0)
cv2.destroyAllWindows()