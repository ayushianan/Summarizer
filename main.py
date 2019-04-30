import os
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import ocr1
from flask import Flask, request, render_template, send_from_directory

__author__ = 'ayushi'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        #print(destination)
        file.save(destination)
        ocr1.find(destination)
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)
