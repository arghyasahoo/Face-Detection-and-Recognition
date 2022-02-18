# Face Detection
"""
Used to detect if the student has left the window or not
"""

# Importing standard libraries
from functools import total_ordering
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

        faces = self.face_cascade.detectMultiScale(
            self.grayscaled, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        total_faces = -1
        try:
            total_faces = len(list(faces))
            # print(
            #     "Total faces:", total_faces
            # )  # returns the face count in an image
        except:
            total_faces = len(list(faces))
            print("Could not find out total number of faces")

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            result = cv.rectangle(
                self.grayscaled, (x, y), (x + w, y + h), (255, 255, 255), 2
            )
        return (result, total_faces)
