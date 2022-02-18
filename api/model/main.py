# Driver Code

from face_detector import FaceDetector
from face_recognizer import FaceRecognizer
import matplotlib.pyplot as plt

import os


def main():
    detected = FaceDetector(
        os.path.abspath(
            "/home/arghya/Github/Face-Detection-and-Recognition/api/upload/7.jpg"
        )
    ).detect()
    # recognized = FaceRecognizer("../../img/5.jpg", "../../img/7.jpg").verify()

    # print("Recognition Status = " + str(recognized))
    print(plt.imshow(detected))
    plt.show()


if __name__ == "__main__":
    main()
