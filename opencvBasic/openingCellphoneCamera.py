import cv2

video = cv2.VideoCapture()

# instale o app 'IP WebCam' na PlayStore
# clique em start server
# copie o ip q possui 'https'
# insira o ip no parametro abaixo

ip = "{your-ip}/video"
video.open(ip)

while True:
    check, img = video.read()
    cv2.imshow("img", img)
    cv2.waitKey(1)