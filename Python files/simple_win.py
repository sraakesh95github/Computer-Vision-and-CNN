import cv2

# Image displays on a separate image
# Image display window is not resizeable
img = cv2.imread('DATA/00-puppy.jpg')

# Note the use of OpenCV to display instead of Matplotlib
while True:
    cv2.imshow('Puppy', img)
    # TImeout
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
        
cv2.destroyAllWindows()
        