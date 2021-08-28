import cv2 as cv

# pylint: disable=no-member
smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_smile.xml")
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect(gray, frame): 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces: 
        cv.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 
  
        for (sx, sy, sw, sh) in smiles: 
            cv.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
    return frame

video_capture = cv.VideoCapture(0) 
while True: 
   # Captures video_capture frame by frame 
    _, frame = video_capture.read()  
  
    # To capture image in monochrome                     
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   
      
    # calls the detect() function     
    canvas = detect(gray, frame)
  
    # Displays the result on camera feed                      
    cv.imshow('Video', canvas)  
  
    # The control breaks once q key is pressed                         
    if cv.waitKey(1) & 0xff == ord('q'):                
        break
  
# Release the capture once all the processing is done. 
video_capture.release()                                  
cv.destroyAllWindows() 
