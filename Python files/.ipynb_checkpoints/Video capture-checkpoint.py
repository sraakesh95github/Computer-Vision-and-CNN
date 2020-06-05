import cv2
import numpy as np

# Grab using the default camers
capture = cv2.VideoCapture(0)

# Set the dimenstions of the image
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) # returns 1080.0p
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print("Wdith:" + str(width))
print("Height:" + str(height))

# Write the stream to a video file
# fourcc encodes the video. Changes based upon the OS
# For the fourcc codec check "fourcc.org"
writer = cv2.VideoWriter("../Outputs/my_video.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

# print(frame_count)

while True:
    ret, frame = capture.read()
    
    # Write the frames into an mp4 file
    writer.write(frame)
    
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    if(cv2.waitKey(2) & 0xFF == ord('q')):
        break
    
capture.release()
writer.release()
cv2.destroyAllWindows

