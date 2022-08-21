import cv2 as cv

img = cv.imread('./photos/face.jpeg')

cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade=cv.CascadeClassifier('./haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)

#draw a rectangle around the faces
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    


print(len(faces_rect))


cv.waitKey(0)
