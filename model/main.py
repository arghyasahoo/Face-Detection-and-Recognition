# Driver Code

from face_detector import FaceDetector
from face_recognizer import FaceRecognizer
import matplotlib.pyplot as plt


def main():
    detected = FaceDetector("../img/5.jpg").detect()
    recognized = FaceRecognizer("../img/5.jpg", "../img/7.jpg").verify()

    print("Recognition Status = " + str(recognized))
    print(plt.imshow(detected))
    plt.show()


if __name__ == "__main__":
    main()
