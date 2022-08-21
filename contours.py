import cv2 as cv
import numpy as np



img = cv.imread('./photos/vscode.png')
cv.imshow("VS Code", img)

blank = np.zeros(img.shape, np.uint8)
cv.imshow("Blank", blank)


#Converting to gray-scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

"""#Blurring

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

#Edge detection
canny = cv.Canny(blur,125,175)
cv.imshow("Canny", canny)"""

ret ,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank, contours,-1,(0,0,255),2)
cv.imshow("Contours", blank)

cv.waitKey(0)