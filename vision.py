import numpy as np
import cv2
import sys
from PIL import *
f=cv2.face.LBPHFaceRecognizer_create()
faceCascade = cv2.CascadeClassifier('visiondata/haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('visiondata/haarcascade_eye.xml')

vid=cv2.VideoCapture(0)
while(vid.isOpened()==True):
    ret,frame = vid.read()
    if(ret==True):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]
            eyes=eyeCascade.detectMultiScale(roi_gray)
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            vid.release()
            break
    else:
        print("No Image")
#cv2.destroyAllWindows()
#vid.release()
