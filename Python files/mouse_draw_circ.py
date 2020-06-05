import cv2
import numpy as np

# Init certain params
window_name = 'My drawing'
static_circle_rad = 30

##############
## FUNCTION ##
##############
def draw_circle(event, x, y, flags, param):
    
    #Please note that the cv2 objects like the cv2.EVENT_LBUTTONDOWN can be obtained by just typing in "cv2.EVENT_L" and pressing the "Tab" button on the keyboard
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, center = (x,y), radius = static_circle_rad, color = (0,255,0), thickness = -1)
        
    elif (event == cv2.EVENT_RBUTTONDOWN):
        cv2.circle(img, center = (x,y), radius = static_circle_rad, color = (255,0,0), thickness = -1)
        
    elif

# Set the name of the window that contains the image
cv2.namedWindow(winname = window_name)

# Mote that setMouseCallback sets all the necessary parameters for the draw_circle function. But, it is necessary to make sure that the called function has the following parameters
# 1. event - the mouse click events
# 2. x, y - the coordinates on the window where the mouse is clicked
# 3. flags - 
# 4. param - additional params as tuple
cv2.setMouseCallback(window_name, draw_circle)

############################
## SHOW IMAGE WITH OPENCV ##
############################

# init image (int8 makes the background look a bit gray)
# Instead ommitting the setting of dtype can make the image appear pure black
img = np.zeros((512, 512, 3))

# Continuously display the image on the screen
while True:
    cv2.imshow(window_name, img)
    
    # Use '27' instead of 'ord('w')' to root for the 'Esc' key on the keyboard in order to exit
    if(cv2.waitKey(20) & 0xFF == ord('q')):
        break