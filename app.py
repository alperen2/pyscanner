import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        if o
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break