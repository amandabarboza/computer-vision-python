import cv2

camera = cv2.VideoCapture(0)
# se tiver duas webcams, utilizar indice 1 ou 2

camera.set(3,640) #largura
camera.set(4,420) #altura
camera.set(10,200) #brilho/luminosidade

while True:
    check,img = camera.read()

    cv2.imshow('Webcam',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
