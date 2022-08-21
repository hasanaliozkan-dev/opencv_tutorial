import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

"""
# 1. Paint the image a certain color
blank[:,:] = 0,255,0 #green
"""

"""
# 2. Draw a rectangle

cv.rectangle(blank, (0,0), (250,250), (0,255,0),thickness=-1) # -1 means filled

"""

"""
# 3. Draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1) # -1 means filled

"""

"""
# 4. Draw a line
cv.line(blank, (100,100), (200,100), (255,255,255), thickness=3) # -1 means filled
"""

#5. Write text
cv.putText(blank, "Hello World", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1, (0,255,0), thickness=2)


cv.imshow('blank', blank)
cv.waitKey(0)
