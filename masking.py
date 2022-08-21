import cv2 as cv
import numpy as np
img = cv.imread('./photos/vscode.png')
cv.imshow("VS Code", img)


blank = np.zeros(img.shape[:2], np.uint8)
cv.imshow("Blank", blank)

#Masking image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked", masked)

#weird shape mask





cv.waitKey(0)