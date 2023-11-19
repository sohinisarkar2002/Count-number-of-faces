import cv2
# import numpy as np
import dlib


# Connect to default camera
cap = cv2.VideoCapture(0)

# Detect coordinates of face
detector = dlib.get_frontal_face_detector()

# Capture frames continuously
while True:

    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert original color to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # To count the number of faces
    cnt = 0
    for face in faces:
        x = face.left()
        y = face.top()
        x1 = face.right()
        y1 = face.bottom()
        # Draw green rectangle around each face detected
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        # Increment cnt for each face
        cnt = cnt + 1

        # Display rectangular box and face numbers
        cv2.putText(frame, "Face no. " + str(cnt), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        print(face, cnt)

    # Display resulting frame
    cv2.imshow("Frame", frame)

    # Break the loop when 'esc' key hit
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

