import cv2

img = cv2.imread('../images/farol.jpg')
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

print(imgCinza)
cv2.imshow('Imagem', img)
cv2.imshow('ImageM Cinza', imgCinza)
cv2.waitKey(0)