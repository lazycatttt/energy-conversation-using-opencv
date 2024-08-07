import cv2
import numpy
import time
import serial

face_cascade = cv2.CascadeClassifier('C:\\Program Files\\Python311\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

SerialObj = serial.Serial('COM4')              
SerialObj.baudrate = 9600  
SerialObj.bytesize = 8   
SerialObj.stopbits = 1
time.sleep(1)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    cv2.line(img, (330,0), (330,600), (0, 0, 255), 6)# y axis
    cv2.line(img, (0,180), (800,180), (0, 0, 255), 6)# x axis
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
        if x<200 and y<100:
            SerialObj.write(b'A')
            #print("1")
        elif x>300 and y<100:
            SerialObj.write(b'B')
            #print("2")
        elif x>300 and y>180:
            SerialObj.write(b'C')
            #print("3")
        elif x<200 and y>200:
            SerialObj.write(b'D')
            #print("4")
        #print(x,"||",y)
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)  # Create a resizable window
    cv2.resizeWindow("Video", 600, 600)  # Set window size      
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
SerialObj.close()         
cap.release()
cv2.destroyAllWindows() 
