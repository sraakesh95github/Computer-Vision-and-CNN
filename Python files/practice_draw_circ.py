import cv2
import matplotlib.pyplot as plt
import numpy as np

# Define variable names
win_name = "draw circles"
img = np.zeros((512, 512, 3))

# Function to reinit the image
def init_img():
    global img
    img = np.zeros((512, 512, 3))

# Define the function that responds to the mouse event trigger
def draw_circ(event, x, y, flags, params):
    
    # Define what happens when a Right mouse click occurs
    if(event == cv2.EVENT_RBUTTONDOWN):
        global img
        init_img()
        # print("Event Triggered...")
        cv2.circle(img, center = (x, y), radius = 30, color = (255, 0, 0), thickness = 2)

# Provide details about the canvas
cv2.namedWindow(win_name)

# Assign the mouse callback event for the particular window
cv2.setMouseCallback(win_name, draw_circ)

# Plot the image on the window
while True:
    cv2.imshow(win_name, img)
    if(cv2.waitKey(2) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()