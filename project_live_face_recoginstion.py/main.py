import cv2 as cv

#Intiliased video capture of webcam 
cap = cv.VideoCapture(0)

#classified the open cv's haar casscade 
haar_cascade = cv.CascadeClassifier('project_live_face_recoginstion.py/haar_face.xml')

#checking if webcam is active 
if not cap.isOpened():
    print('Cant open your camera')


while True:
    #using read we get our webcams current frame 
    ret,frame  = cap.read()
    if not ret:
        print('Cant recieve frame')

    #changing BGR frame to GRAY scale 
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #using the haar cascade on the gray scale image 
    face_detect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10)
    #adjust the scalefactor and minNeighbors for more accuracy 

    #drawing a rectangle around ROI
    for (x,y,w,h) in face_detect:
        cv.rectangle(frame, (x,y), (x + w, y+h), (0,255,0), thickness=5)

    #putting the text of number of faces 
    cv.putText(frame, f'Total Faces:{len(face_detect)}', (40,40), cv.FONT_HERSHEY_DUPLEX, fontScale=2.0, color=(0,0,139), thickness=5)
    
    #displaying the image 
    cv.imshow('detect', frame)

    #checking for waitkey
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#releasing cap and destroying all windows 
cap.release()
cv.destroyAllWindows()
