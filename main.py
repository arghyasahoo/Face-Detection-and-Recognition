# Driver Code

from face_detector import FaceDetector
from face_recognizer import FaceRecognizer


def main():
    detected = FaceDetector("img/5.jpg")
    recognized = FaceRecognizer("img/5.jpg", "img/7.jpg")

    print(detected, recognized)


if __name__ == "__main__":
    main()
