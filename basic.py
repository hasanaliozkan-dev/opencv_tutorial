import cv2 as cv

img = cv.imread('./photos/vscode.png')

#Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blurring image
blurred = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blurred)
# Edge cascade

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

#Resize the image
resized = cv.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

#Cropping the image
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

#Showing image
cv.imshow("VS Code", img)
cv.waitKey(0)