import cv2
import numpy as np

# Variables
window_name = "Mouse event"
# true when mouse button down and false when up
drawing = False
ix, iy = (-1, -1)

img = np.zeros((512, 512, 3))

# Function
def img_init():
    global img
    img=np.zeros((512, 512, 3))
    
def draw_rect(event, x, y, flags, params):
        global ix, iy, drawing
        
        if(event == cv2.EVENT_LBUTTONDOWN):
            drawing = True
            ix, iy = (x, y)
            img_init()
        
        elif(event == cv2.EVENT_MOUSEMOVE):
            if(drawing == True):
                cv2.rectangle(img, (ix, iy), (x, y), color = (255, 0, 0), thickness = -1)
        
        elif(event == cv2.EVENT_LBUTTONUP):
            drawing = False
            cv2.rectangle(img, (ix, iy), (x, y), color = (255, 0, 0), thickness = -1)
                
# Canvas
cv2.namedWindow(winname = window_name)
cv2.setMouseCallback(window_name, draw_rect)

# Image Display
while True:
    cv2.imshow(window_name, img)
    if(cv2.waitKey(5) & 0xFF == ord('q')):
        break
        
cv2.destroyAllWindows()

# NOte: Doesn;t work when the mouse pointer is moved backwards beyond the top left point