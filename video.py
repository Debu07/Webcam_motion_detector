import cv2
video=cv2.VideoCapture(0)
count=0
while True:
    count+=1
    check , frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("capturing",gray)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(count)
video.release()
cv2.destroyAllWindows()
