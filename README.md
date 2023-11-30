# Wechat-QR-reader-Dockerization
Docker images are immutable, which means they can't be modified once created. If changes need to be made to an image, you must create a new image with the desired modifications. In contrast, containers are mutable and allow modifications during runtime.


### Docker from docker hub
```
docker pull gautamhcscv/flask-qr-app
docker run --name image-qr-app -p 5001:5001 gautamhcscv/flask-qr-app
```

Docker pushed in public domain.
