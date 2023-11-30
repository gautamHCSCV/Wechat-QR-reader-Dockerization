import cv2
import os
import numpy as np
from collections import defaultdict

detector = cv2.wechat_qrcode_WeChatQRCode(
        "detect.prototxt", "detect.caffemodel", "sr.prototxt", "sr.caffemodel")

d = defaultdict(lambda: 0)
path = "C:/Users/GAUTAM/Downloads/Static Captured Images 25mm/"
cnt = 0
for img in os.listdir(path):
    image_path = path+f'{img}'
    image = cv2.imread(image_path)
    qr_codes, points = detector.detectAndDecode(image)
    if not qr_codes:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        qr_codes, points = detector.detectAndDecode(image)
    if qr_codes:
        #print(qr_codes[0])
        d[len(qr_codes[0])]+=1
        cnt+=1
    else:
        print(img)
print(len(os.listdir(path)),cnt)
print(d)