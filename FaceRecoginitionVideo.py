import cv2

# Load the cascade# Load the cascade, which has a bunch of claassifers that are used to detect faces 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cv2 is used to capture the video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale which is needed by cv2
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #it is used to detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # draws the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display the rectangle
    cv2.imshow('img', img)

    # stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# realses video capture
cap.release()