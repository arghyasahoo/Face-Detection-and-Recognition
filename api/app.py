# Importing custiom libraries
from model.face_detector import FaceDetector
from model.face_recognizer import FaceRecognizer

# Importing flask
from flask import Flask, request
from werkzeug.utils import secure_filename

# Importing standard libraries
import os


app = Flask(__name__)

UPLOAD_FOLDER = "./upload"
ORIGINAL_FOLDER = "./upload/original"
RESULT_FOLDER = "./results"
ALLOWED_FILE_FORMATS = {"jpg", "png"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ORIGINAL_FOLDER"] = ORIGINAL_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER


@app.route("/", methods=["GET"])
def welcome():
    return "API Running"


def allowed_file(filename):
    if filename.count(".") != 1:
        return False

    if filename.rsplit(".", 1)[1].lower() not in ALLOWED_FILE_FORMATS:
        return False

    return True


@app.route("/original", methods=["POST"])
def original():
    if request.method != "POST":
        return "<h1>Method not Allowed</h1>"

    if "file" not in request.files:
        err_msg = {"error": "[-] File not Found"}
        return err_msg

    image = request.files["file"]

    if image.filename == "":
        err_msg = {"error": "[-] Empty filename"}
        return err_msg

    # image filename must be separately identiiable like begining with 'orig'
    if image and allowed_file(image.filename):
        try:
            # filename = secure_filename(image.filename)
            # filename = "orig_" + filename
            filename = secure_filename(
                "orig_image.jpg"
            )  # default filename for original uploaded image
            image_name = os.path.join(app.config["ORIGINAL_FOLDER"], filename)
            image_name = os.path.abspath(image_name)
            image.save(image_name)
            msg = {"success": "[+] Original Face Detected and Saved"}
        except:
            msg = {"failure": "[-] Could not save Original Image"}

        return msg


def recognize_face(curr_image):
    orig_image_path = ORIGINAL_FOLDER + "/orig_image.jpg"
    print(orig_image_path)
    orig_image = open(orig_image_path, "rb").read()
    recognized = FaceRecognizer(curr_image, orig_image)
    orig_image.close()
    print("Done")
    return recognized


@app.route("/detect", methods=["POST"])
def detect_face():
    if request.method != "POST":
        return "<h1>Method not Allowed</h1>"

    if "file" not in request.files:
        err_msg = {"error": "[-] File not Found"}
        return err_msg

    image = request.files["file"]

    if image.filename == "":
        err_msg = {"error": "[-] Empty filename"}
        return err_msg

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_name = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        image_name = os.path.abspath(image_name)
        image.save(image_name)

        try:
            result = FaceDetector(image_name).detect()
            recognize_face(image_name)  # * if detected, recognize face
            msg = {"success": "[+] Face detected and recognized"}
        except:
            msg = {"error": "Face not detected"}

        return msg
