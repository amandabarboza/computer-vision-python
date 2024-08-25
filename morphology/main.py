import cv2

img = cv2.imread('../images/piramide.jpg')
img = cv2.resize(img,(500,400))
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgCinza,(7,7),0)
imgCanny = cv2.Canny(img,50,100)
imgDilat = cv2.dilate(imgCanny,(5,5),iterations=5)
imgErode = cv2.erode(imgCanny,(5,5),iterations=2)
imgOpening = cv2.morphologyEx(imgCanny,cv2.MORPH_OPEN,(5,5))
imgClosing = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(5,5))

cv2.imshow('Img Original',img)

#mostrando cinza
cv2.imshow('Img Cinza',imgCinza)

#mostrando com blur
cv2.imshow('Img Blur',imgBlur)

#mostrando apenas contornos
cv2.imshow('Img Canny',imgCanny)

#dilata/expande todos os pontos da imagem, a partir do canny
cv2.imshow('Img Dilat',imgDilat)

#tende a criar uma erosão, desfragmentando os objetos
cv2.imshow('Img Erode',imgErode)
cv2.imshow('Img Open',imgOpening)
cv2.imshow('Img Close',imgClosing)


cv2.waitKey(0)
