from curses.textpad import rectangle
import cv2 as cv
import numpy as np
blank = np.zeros((400,400), np.uint8)

#Rectangle
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv.imshow("Rectangle", rectangle)

#Circle
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("Circle", circle)

#bitwise_and intersection
bitwise_and = cv.bitwise_and(circle,rectangle)
cv.imshow("Bitwise_and", bitwise_and)

#bitwise_or union
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow("Bitwise_or", bitwise_or)

#bitwise_xor non-intersection
bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow("Bitwise_xor", bitwise_xor)


#bitwise_not complement
bitwise_not = cv.bitwise_not(circle)
cv.imshow("Bitwise_not", bitwise_not)



#Line
line = cv.line(blank,(0,0),(400,400),(255,255,255),5)
cv.imshow("Line", line)

#Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
polygon = cv.polylines(blank,[pts],True,(255,255,255))
cv.imshow("Polygon", polygon)




cv.waitKey(0)