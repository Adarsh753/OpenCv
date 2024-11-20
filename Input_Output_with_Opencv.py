# This file is used to practice Input/Output of an image with OpenCV
import cv2

#read an image
img_path = r"D:/OpenCv/Resources/Bird.jpg"
img = cv2.imread(img_path)

#read a video
Vid_path = r"D:/OpenCv/Resources/big_buck_bunny_480p_1mb.mp4"
Video = cv2.VideoCapture(Vid_path)

#read from webcam
webcam = cv2.VideoCapture(0)

#write an image
img2=cv2.imwrite(r'D:/OpenCv/Resources/Bird_write.jpeg',img)

#visualize an image

cv2.imshow('Bird',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#visualize video
ret =  True
while ret:
    ret , frame = Video.read()

    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(40)
        
Video.release()
cv2.destroyWindow(frame)

#visualize webcam video


while True:
    ret , frame = webcam.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyWindow(frame)
