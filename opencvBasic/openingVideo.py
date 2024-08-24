import cv2

video = cv2.VideoCapture('../videos/runners.mp4')

while True:
    check,img = video.read()
    imgRedim = cv2.resize(img,(640,420))
    cv2.imshow('video',imgRedim)
    cv2.waitKey(10)