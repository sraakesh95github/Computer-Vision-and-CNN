import cv2

## Callback function for drawing the rectangle
def draw_rect(event, x, y, flags, param):
    
    global pt1, pt2, topLeft_clicked, bottomRight_clicked
    
    if(event == cv2.EVENT_LBUTTONDOWN):
        
        # Nothing has been clicked
        if(topLeft_clicked == False):
            topLeft_clicked = True
            pt1 = (x,y)
            
        # Top left has been clicked
        elif(bottomRight_clicked == False):
            bottomRight_clicked = True
            pt2 = (x,y)
        
        # Reset the rectangle
        else:
            topLeft_clicked = False
            bottomRight_clicked = False
            pt1 = (0,0)
            pt2 = (0,0)

## Global variables
pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
bottomRight_clicked = False

## Connect to the callback
cap = cv2.VideoCapture(0)
           
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rect)
    
while True:
    ret, frame = cap.read()
             
    ## Draw the frame based on the global variables
    if(topLeft_clicked == True):
        # To show where the mouse has been clicked
        cv2.circle(frame, pt1, radius = 5, color = (0,0,255), thickness = -1)
        
    if(topLeft_clicked & bottomRight_clicked):
        cv2.rectangle(frame, pt1, pt2, color = (0,255,0), thickness = 3)
        
    cv2.imshow('Test', frame)
             
    if(cv2.waitKey(2) & 0xFF == ord('q')):
        break
             
cap.release()
cv2.destroyAllWindows()