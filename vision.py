import numpy as np
import cv2
import sys
import time
from PIL import *
import json
from datetime import datetime

detected=True
curr=(datetime.now()).seconds

def alert(date,img):
    global detected
    if(detected==True):
        detected=False
        #date=datetime.now()
        exactTime=date.strftime("%X")
        day=date.strftime("%a")
        month=date.strftime("%b")
        year=date.strftime("%Y")
        print(exactTime+" " + day +" " + month + " " +year)

f=cv2.face.LBPHFaceRecognizer_create()
faceCascade = cv2.CascadeClassifier('visiondata/haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('visiondata/haarcascade_eye_tree_eyeglasses.xml')
timecaught=0
vid=cv2.VideoCapture(0)
while(vid.isOpened()==True):
    ret,frame = vid.read()
    if(ret==True):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            curr=datetime.now()
            alert(curr,"hello")
            #edge case with midnight need to do
            '''if(curr-timecaught>3) and (curr-timecaught<300):
                #Alert Person at door and stop counting time for a little
                alert("hello")
            timecaught=curr
            '''
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]
            eyes=eyeCascade.detectMultiScale(roi_gray)
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break
    else:
        print("No Image")
vid.release()
cv2.destroyAllWindows()
sys.exit(0)