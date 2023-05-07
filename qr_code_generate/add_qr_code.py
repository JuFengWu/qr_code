import cv2

addImg = cv2.imread('qrcode.png')
foreground = cv2.imread('logo.jpg')
addImg = cv2.resize(addImg,(150,150))
rows, cols, channels = addImg.shape
foreground[foreground.shape[0]-rows:foreground.shape[0], foreground.shape[1]-cols:foreground.shape[1]] = addImg
cv2.imwrite('result.jpg', foreground)