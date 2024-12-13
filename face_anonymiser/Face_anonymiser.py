import cv2

# Read video
Face = cv2.VideoCapture(r"D:\OpenCv\Resources\8090193-uhd_4096_2160_25fps.mp4")

# Check if the video opened correctly
if not Face.isOpened():
    print("Error: Couldn't open video.")
else:
    # Load the pre-trained Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = Face.read()  # Read frame-by-frame

        if not ret:
            print("Error: Failed to read frame from the video.")
            break

        # Convert to greyscale
        grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the frame (optional)
        resized_frame = cv2.resize(frame, (640, 360))  # Resize to a smaller resolution (640x360)
        h, w = resized_frame.shape[:2]

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Debugging: Print number of faces detected and coordinates
        print(f"Faces detected: {len(faces)}")
        for (x, y, w, h) in faces:
            print(f"Face coordinates: x={x}, y={y}, w={w}, h={h}")

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            # Ensure the rectangle is drawn correctly on the resized frame
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Change to a more visible color (yellow)

        # Show the original frame with face detection
        cv2.imshow('Normal Video', resized_frame)  # Show the resized original frame with face detection
        cv2.imshow('Greyscale Video', grey_img)    # Show the grayscale frame

        # Exit if the 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII for the 'Esc' key
            break

    # Release the video capture object and close all windows
    Face.release()
    cv2.destroyAllWindows()
