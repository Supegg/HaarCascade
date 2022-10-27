import cv2

face_cascade = cv2.CascadeClassifier(
    r"classifier\cascade.xml")  # path of cascade file
# following is an test image u can take any image from the p folder in the temp folder and paste address of it on below line
# path of image file which we want to detect
img = cv2.imread(r"p\1588088902809.jpg")
resized = cv2.resize(img, (400, 200))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# try to tune this 6.5 and 17 parameter to get good result
faces = face_cascade.detectMultiScale(gray, 6.5, 17)
# if not getting good result try to train new cascade.xml file again deleting other file expect p and n in temp folder
for (x, y, w, h) in faces:
    resized = cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('img', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
