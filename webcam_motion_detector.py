import cv2
first_frame=None
video=cv2.VideoCapture(0)
while True:
    check , frame=video.read()
    status=0
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.GaussianBlur(gray_frame,(21,21),0)
    if first_frame is None:
        first_frame=gray_frame
        continue
    diff_frame=cv2.absdiff(first_frame,gray_frame)
    threshhold_frame=cv2.threshold(diff_frame,30,255,cv2.THRESH_BINARY)[1]
    threshhold_frame=cv2.dilate(threshhold_frame,None,iterations=2)
    (cnts,_)=cv2.findContours(threshhold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("Gray Frame",gray_frame)
    cv2.imshow("Difference Frame",diff_frame)
    cv2.imshow("THreshhold Frame",threshhold_frame)
    cv2.imshow("Colour Frame",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    print(status)
video.release()
cv2.destroyAllWindows()

