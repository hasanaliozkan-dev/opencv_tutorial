import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('./photos/vscode.png')
cv.imshow("VS Code", img)


blank = np.zeros(img.shape[:2], np.uint8)
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, 2)
cv.imshow("Mask", circle)

masked = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Masked", masked)
#Grayscale histogram
hist = cv.calcHist([gray], [0], masked, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

#Color histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i],None, [256], [0, 256])
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
    plt.show()


cv.waitKey(0)