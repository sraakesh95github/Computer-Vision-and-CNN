import cv2
import time

capture = cv2.VideoCapture('../Outputs/my_video.mp4')

if(capture.isOpened() == False):
    print("Error: File not found / wrong codec used")
    
while(capture.isOpened):
    ret, frame = capture.read()
    
    if ret==True:
        cv2.imshow('frame', frame)
        if(cv2.waitKey(2) & 0xFF == ord('q')):
            break
        
        # Writer 20 fps ; This is inserted to only display the video
        # Must not be given while processing
        time.sleep(1/20)
        
    else:
        break

capture.release()
cv2.destroyAllWindows()        