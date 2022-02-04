# Face Detection
"""
Used to detect if the student has left the window or not
"""

# Importing standard libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


class FaceDetector:
    def __init__(self, image) -> None:
        self.face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.image = image
        self.grayscaled = cv.cvtColor(cv.imread(self.image), cv.COLOR_BGR2GRAY)

    def detect(self):
        faces = self.face_cascade.detectMultiScale(
            self.grayscaled, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            result = cv.rectangle(
                self.grayscaled, (x, y), (x + w, y + h), (255, 255, 255), 2
            )
        return result
