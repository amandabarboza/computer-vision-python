import cv2

# img = cv2.imread("../images/piramide.jpg")

video = cv2.VideoCapture("../videos/runners.mp4")

while True:
    check,img = video.read()

    cv2.rectangle(img,(50,50),(200,200),(255,0,0),5)

    cv2.circle(img,(300,300),50,(0,0,255),-1)
    # se utilizar -1 na espessuram, a forma ficará preenchida pela cor

    cv2.line(img,(300,400),(500,300),(0,255,0),2)


    texto = 'Piramides do Egito'
    cv2.putText(img,texto,(200,230),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,0,0),3)

    cv2.imshow('Imagem',img)
    cv2.waitKey(10)