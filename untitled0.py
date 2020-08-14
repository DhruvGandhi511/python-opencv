# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:37:58 2020

@author: DHRUV
"""

import cv2
import numpy as np
img = cv2.imread('pop.png')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()