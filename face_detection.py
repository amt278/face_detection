import pathlib
import cv2

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / 'data/haarcascade_frontalface_default.xml'
# print(cascade_path)

clf = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0) # ashan ashaghal el camera (0 = default camera)
# camera = cv2.VideoCapture("video.mp4") # lw ayez a3mlo 3la video

while True:
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)

    cv2.imshow("faces", frame)
    if cv2.waitKey(1) == ord('q'): # lw dost 3la Q
        break

camera.release()
cv2.destroyAllWindows()