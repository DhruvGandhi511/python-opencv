import cv2
import numpy as np

draw = False

def nothing(x):
    pass

def draw_line(event,x,y,flags,param):
    global draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(img, (x,y),t,(b,g,r),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
    else:
        pass

def get_tar():
    global r,g,b,s,t
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    t = cv2.getTrackbarPos('T','image')


img = np.zeros((300,512,3),np.uint8)
img[:] = 255
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('T','image',0,20,nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

 # get current positions of five trackbars
    get_tar()

    if s == 0:
        img[:] = 255
        draw = False
    else:
        cv2.setMouseCallback('image', draw_line)

cv2.destroyAllWindows()