# Driver Code

from face_detector import FaceDetector
from face_recognizer import FaceRecognizer
import matplotlib.pyplot as plt

import os


def main():
    detected = FaceDetector(os.path.abspath("/home/arghya/Pictures/img/7.jpg")).detect()
    # recognized = FaceRecognizer(
    #     "/home/arghya/Pictures/img/7.jpg", "/home/arghya/Pictures/img/5.jpg"
    # ).verify()

    # print(recognized)

    # print("Recognition Status = " + str(recognized))
    print(plt.imshow(detected[0]))
    plt.show()


if __name__ == "__main__":
    main()
