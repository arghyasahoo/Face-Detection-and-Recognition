# Face Detection
"""
Used to detect if the student has left the window or not
"""

# Importing standard libraries
import cv2 as cv


class FaceDetector:
    def __init__(self, image) -> None:
        # image = "/home/arghya/Github/Face-Detection-and-Recognition/api/upload/7.jpg"
        self.face_cascade = cv.CascadeClassifier(
            "/home/arghya/Github/Face-Detection-and-Recognition/api/model/haarcascade_frontalface_default.xml"  # * change this to absolute path of the file in the api server
        )
        self.image = cv.imread(image)
        self.grayscaled = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

    def detect(self):
        result = None

        # print("\n==========Original Image==========\n")
        # print(self.image)
        # print("\n==========Grayscaled Image==========\n")
        # print(self.grayscaled)

        # ! path error occuring here
        faces = self.face_cascade.detectMultiScale(
            self.grayscaled, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        try:
            print(
                "Total faces:", len(list(faces))
            )  # returns the face count in an image
        except:
            print("Could not find out total number of faces")
            pass

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            result = cv.rectangle(
                self.grayscaled, (x, y), (x + w, y + h), (255, 255, 255), 2
            )
        return result
