import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('/Users/syedrihaanshah/Python-Projects/project_live_face_recoginstion.py/haar_face.xml')

if not cap.isOpened():
    print('Cant open your camera')

while True:
    ret,frame  = cap.read()
    if not ret:
        print('Cant recieve frame')
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face_detect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10)

    for (x,y,w,h) in face_detect:
        cv.rectangle(frame, (x,y), (x + w, y+h), (0,255,0), thickness=5)

    cv.putText(frame, f'Total Faces:{len(face_detect)}', (40,40), cv.FONT_HERSHEY_DUPLEX, fontScale=2.0, color=(0,0,139), thickness=5)
    
    cv.imshow('detect', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
