import cv2
import numpy as np

# Define the color ranges for red, yellow, and green
lower_red = np.array([0, 120, 70]) # Lower bound for red
upper_red = np.array([10, 255, 255]) # Upper bound for red

lower_yellow = np.array([20, 100, 100]) # Lower bound for yellow
upper_yellow = np.array([30, 255, 255]) # Upper bound for yellow

lower_green = np.array([40, 50, 50]) # Lower bound for green
upper_green = np.array([90, 255, 255]) # Upper bound for green

cap = cv2.VideoCapture(r"c:\Users\Asus\Downloads\3087320-uhd_3840_2160_30fps.mp4") # Replace with your video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize the frame to a smaller size for faster processing
    resized_frame = cv2.resize(frame, (640, 480))

    # Convert the frame to HSV color space
    hsv_img = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)

    # Create masks for each color range
    mask_red = cv2.inRange(hsv_img, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv_img, lower_green, upper_green)

    # Find contours for red, yellow, and green
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process contours for each color
    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 500: # Ignore small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(resized_frame, "Red Light", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    for contour in contours_yellow:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(resized_frame, "Yellow Light", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    for contour in contours_green:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(resized_frame, "Green Light", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Traffic Light Detection", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()