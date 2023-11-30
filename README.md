# Wechat-QR-reader-Dockerization
Docker images are immutable, which means they can't be modified once created. If changes need to be made to an image, you must create a new image with the desired modifications. In contrast, containers are mutable and allow modifications during runtime.


### Docker from docker hub
```
docker pull gautamhcscv/flask-qr-app
docker run --name image-qr-app -p 5001:5001 gautamhcscv/flask-qr-app
```

Docker pushed in public domain.

```
import requests

url = "http://127.0.0.1:5001/inference"
payload = {}
files=[
  ('image',('Image__2023-10-31__16-13-00.bmp',open(r"C:/Users/GAUTAM/Downloads/Static Captured Images 25mm/Image__2023-10-31__16-13-00.bmp",'rb'),'image/bmp'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

```
