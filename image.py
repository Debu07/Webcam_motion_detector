import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("multiple.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(15,22,14),2)
print(type(faces))
print(faces)
resized_image=cv2.resize(img,(700,550))
cv2.imshow("myphoto",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()