import cv2
import numpy as np
import matplotlib.pyplot as plt

# Detect the corners of the object to get the points to be tracked

# Set the params for the corner detection
corner_track_params = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)

# Setup the Lucas Kanade params
# Smaller windows - more sensitive to noise ; miss on larger motions
# Larger windows - smaller motion of points may not be detected
# maxLevel - Pyramid for image processing ; Change in the resolution of the image l Eg : maxLevel 2 has a resolution 1/4 the resolution of the original image
# Term criteria epsilon EPS from paper - Here 0.03 - Smaller epsilon means less time required for completion
# Term criteria count - max number of iterations (Here 10) ; The search for the points iterations for determined by this
# Exchanges speed of the trackinf with the accuracy of the tracking
lk_params = dict(winSize = (200, 200), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Get an image from a video file
cap = cv2.VideoCapture('test1.mp4')

# get the previous frame from the video
ret, prev_frame = cap.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Get the points to track; use the points from the corner detector
prevPts = cv2.goodFeaturesToTrack(prev_gray, mask=None, **corner_track_params)

# Create a mask with an image of zeros with the same dimensions as that of the previous frame
mask = np.zeros_like(prev_frame)

# Loop for running the video
while True:
    
    # This is the current frame
    ret, frame = cap.read()
    
    # Current grayscale frame
    frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate the optical flow on the current frame wrt to the previous frame ; "PyrLK" refers to Pyramid Lucas Kanade
    # None refers to the next points which is spit out by the function
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prevPts, None, **lk_params)
    
    # The returned "status" is a vector which provides the output as '1' if the point corresponding to a particular feature has been found
    good_new = nextPts[status == 1]
    good_prev = prevPts[status == 1]
    
    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        
        # Calculate the x and y positions
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()
        
        # Create a mask and draw the lines ; These 10 lines connects the previous points' position to the current points' position
        mask = cv2.line(mask, (x_new, y_new), (x_prev, y_prev), (0,255,0), 3)
        
        # On current frame draw a dot for the current point of tracking
        frame = cv2.circle(frame, (x_new, y_new), 8, (0,0,255), -1)
        
    # Display the image
    img = cv2.add(frame, mask)
    cv2.imshow('Tracking', img)
    
    # Exit the display
    k = cv2.waitKey(30) & 0xFF
    if k == ord('q'):
        break
        
    prev_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1,1,2)
    
cv2.destroyAllWindows()
cap.release()