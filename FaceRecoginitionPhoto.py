import cv2

# Load the cascade, which has a bunch of claassifers that are used to detect faces 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# This will read the input for any image to be inserted
img = cv2.imread('faces.jpg')

#Convert into grayscale which is needed for cv2
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# This is used to draw rectangle around the faces in the image
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Displays the output
cv2.imshow('img', img)
cv2.waitKey()
