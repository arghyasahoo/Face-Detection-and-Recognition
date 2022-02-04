# Face Recognition
"""
Used to detect if the student has left the window or not
"""

# Importing standard libraries
from deepface import DeepFace
import cv2 as cv
import matplotlib.pyplot as plt


class FaceRecognizer:
    def __init__(self, curr_img, orig_img) -> None:
        self.curr_image = curr_img
        self.orig_image = orig_img
        self.build_model()
        self.verify()

    def build_model(self, rec_model="VGG-Face"):
        model_name = rec_model
        model = DeepFace.build_model(model_name)

    def verify(self):
        result = DeepFace.verify(self.orig_image, self.curr_image)
        return result.get("verified")
