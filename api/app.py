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
RESULT_FOLDER = "./results"
ALLOWED_FILE_FORMATS = {"jpg", "png", "jpeg"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

def saveImg(filename, image):
    if image and allowed_file(filename):
        try:
            fname = secure_filename(filename)
            image_name = os.path.join(app.config["UPLOAD_FOLDER"], fname)
            image_name = os.path.abspath(image_name)
            image.save(image_name)
            return image_name
        except:
            pass
    else:
        return None

def allowed_file(filename):
    if filename.count(".") != 1:
        return False
    if filename.rsplit(".", 1)[1].lower() not in ALLOWED_FILE_FORMATS:
        return False
    return True

@app.route("/", methods=["GET"])
def welcome():
    return "API Running"

@app.route("/recognize", methods=["POST"])
def recognize():
    image1 = request.files["file1"]
    image2 = request.files["file2"]
    curr_image = saveImg(image1.filename, image1)
    orig_image = saveImg(image2.filename, image2)
    try:
        recognized = FaceRecognizer(curr_image, orig_image).verify()
        print(recognized)
        return {"status":recognized}
    except:
        return {"status":False}
    finally:
        os.unlink(curr_image)
        os.unlink(orig_image)


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

    image_name = saveImg(image.filename, image)
    if image_name is not None:
        try:
            # print(image_name)
            detected = FaceDetector(image_name).detect()
            # recognized = recognize_face(image_name)  # * if detected, recognize face

            if len(list(detected[0])) > 0:
                if detected[1] == 0:
                    return {"error": "NFD"}
                elif detected[1] > 1:
                    msg = {"error": "MFD"}
                else:
                    msg = {"success": "OK"}
                    # if recognized:
                    #     msg = {"success": "OK"}
                    # else:
                    #     msg = {"error": "FNR"}
            else:
                msg = {"error": "FND"}

        except:
            msg = {"error": "EXPT"}

        finally:
            os.unlink(image_name)

        return msg
    else:
        return {"error": "FNA"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


"""
OK = Face Detected and Recognized
FND = Face Not Detected
FNR = face Not Recognized
MFD = Multiple Face Detected
FNA = File Not Allowed
"""
