import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture('test.mp4')

i=0

while True:
    
    ret, frame = cap.read()
    #cv2.imwrite('test' + str(i) + '.jpg', frame)
    cv2.imshow('Video Playback', frame)
    k = cv2.waitKey()
    if(k==ord('q')):
        break

print("Total #frames: " + str(i))
cap.release()
cv2.destroyAllWindows()