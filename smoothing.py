import cv2 as cv



img = cv.imread('./photos/vscode.png')
cv.imshow("VS Code", img)

#Averaging
blur = cv.blur(img,(3,3))
cv.imshow("Averaging", blur)

#Gaussian Blur
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian", gaussian)

#Median Blur
median = cv.medianBlur(img,3)
cv.imshow("Median", median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)