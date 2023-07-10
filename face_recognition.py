import cv2

# create classifiers
face_classifier = cv2.CascadeClassifier('opencv_data_haarcascades/haarcascade_eye.xml')
eye_classifier = cv2.CascadeClassifier('opencv_data_haarcascades/haarcascade_frontalface_default.xml')

# read image, convert to greyscale, run classifier
image = cv2.imread('SET_IMAGE')
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = face_classifier.detectMultiScale(image_grey, 1.1, 4)

# create rectangles
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
    roi_grey = image_grey[y : y + h, x : x + w]
    roi_color = image[y : y + h, x : x + w]
    eyes = eye_classifier.detectMultiScale(roi_grey)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
    
# show final image
cv2.imshow('img', image)
cv2.waitKey()