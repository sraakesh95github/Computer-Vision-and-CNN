import cv2
import numpy as np
import matplotlib.pyplot as plt

road = cv2.imread('../DATA/road_image.jpg')

road_copy = np.copy(road)
#plt.imshow(road_copy)

print(road.shape[:2])
print(road.shape)

marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)

# Use qualitative color mapping from matplotlib color mapping
from matplotlib import cm

print("Color mapping for 0th index (R, G, B, Alpha): " + str(cm.tab10(0)))

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

colors=[]

for i in range(10):
    colors.append(create_rgb(i))
    
print(colors)

# Global variables

# #Markers
num_markers = 10 #0-9

# Color choice
current_marker = 1

# Markers updated by Watershed
markers_updated = False

# Call back function

def mouse_callback(event, x, y, flags, param):
    global markers_updated
    
    # Marker to be passed on to the Watershed algorithm
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image, (x,y), 10, (current_marker), -1)
        
        # User sees on the road image
        cv2.circle(road_copy, (x,y), 10, colors[current_marker], -1)
    
        markers_updated = True
    
# Continuous run (While True statement)
cv2.namedWindow('Road Image')
# Starts the event to check whether there has been a mouse_callback on the image or not
cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Road Image', road_copy)
    
    # Close all windows
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    
    # Clear all the colors
    elif k == ord('c'):
        road_copy = road.copy()
        
        # Init the images to have them cleared
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype = np.uint8)
    
    # Update the color choice
    # 'chr' converts the ASCII into an actual character
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
        
    # Update the markings
    if markers_updated:
        marker_copy = marker_image.copy()
        cv2.watershed(road, marker_copy)
        
        segments = np.zeros(road.shape, dtype = np.uint8)
        
        for color_ind in range(num_markers):
            
            # Coloring the segments - NumPy call
            segments[marker_copy == (color_ind)] = colors[color_ind]
        
cv2.destroyAllWindows()