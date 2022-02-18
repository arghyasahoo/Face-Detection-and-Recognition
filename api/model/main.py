# Driver Code

from face_detector import FaceDetector
from face_recognizer import FaceRecognizer
import matplotlib.pyplot as plt

import os


def main():
    # detected = FaceDetector(
    #     os.path.abspath(
    #         "/home/arghya/Github/Face-Detection-and-Recognition/api/upload/7.jpg"
    #     )
    # ).detect()
    recognized = FaceRecognizer(
        "/home/arghya/Github/Face-Detection-and-Recognition/api/upload/7.jpg",
        "/home/arghya/Github/Face-Detection-and-Recognition/api/upload/5.jpg",
    ).verify()

    print(recognized)

    # print("Recognition Status = " + str(recognized))
    # print(plt.imshow(detected))
    # plt.show()


if __name__ == "__main__":
    main()
