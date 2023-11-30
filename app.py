from flask import Flask, request, jsonify, make_response
import os
import requests
import numpy as np
import cv2
from io import BytesIO
from datetime import datetime
import csv

print(cv2.__version__)

detector = cv2.wechat_qrcode_WeChatQRCode(
        "detect.prototxt", "detect.caffemodel", "sr.prototxt", "sr.caffemodel")

app = Flask(__name__)

    
@app.route("/inference", methods=["POST"])
def inference_endpoint():
    input_image = request.files[f"image"]
    #print(np.frombuffer(input_image.read(), np.uint8).shape)
    image = cv2.imdecode(np.frombuffer(input_image.read(), np.uint8), cv2.IMREAD_COLOR)
    qr_codes, points = detector.detectAndDecode(image)
    if not qr_codes:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        qr_codes, points = detector.detectAndDecode(image)
    if qr_codes:
        return(qr_codes[0])
    return '0'

if __name__ == "__main__":
  app.run(host ='0.0.0.0', port = 5001, debug = True)
