
import cv2 as cv
#Reading image
"""img = cv.imread('./photos/vscode.png')

#Showing image
cv.imshow("VS Code", img)
cv.waitKey(0)


#Reading videos
#  

capture = cv.VideoCapture("Path")
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()"""

#Resizing , rescaling image and video


def changeResolution(width,height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)

def rescaleFrame(frame,scale=0.75):
    #images , videos, live video

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)

    return cv.resize(frame,dim, interpolation=cv.INTER_AREA)


img = cv.imread('./photos/vscode.png')
resized_img = rescaleFrame(img,scale=2)
#Showing image
cv.imshow("VS Code", img)
cv.imshow("VS Code1", resized_img)

"""capture = cv.VideoCapture("Path")
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("Video", resized_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()"""

cv.waitKey(0)