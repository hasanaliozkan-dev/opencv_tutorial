import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('./photos/vscode.png')
cv.imshow("VS Code", img)

#BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#BGR to LAB l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()

#HSV to BGR
bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("BGR", bgr)

#LAB to BGR
bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("BGR", bgr)


cv.waitKey(0)