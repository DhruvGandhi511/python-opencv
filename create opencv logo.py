import cv2
import numpy as np

img=np.zeros((500,500,3), np.uint8)

cv2.ellipse(img, (250,100), (70,70), 135, 0, 270, (0,0,255),50)
cv2.ellipse(img, (150,280), (70,70), 10, 0, 270, (0,255,0),50)
cv2.ellipse(img, (350,280), (70,70), 315, 0, 270, (255,0,0),50)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(75,450), font, 3,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()