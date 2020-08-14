# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:05:21 2020

@author: DHRUV
"""


import numpy as np
import cv2 as cv
    
   
def draw_circle(event,x,y,flags,param):
     
     if event == cv.EVENT_LBUTTONDBLCLK:
         
          cv.circle(img,(x,y),100,(255,0,0),-1)
    

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
    
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        
        break
cv.destroyAllWindows()