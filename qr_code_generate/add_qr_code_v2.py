import cv2

addImg = cv2.imread('qrcode.png')
foreground = cv2.imread('logo.jpg')
addImg = cv2.resize(addImg,(150,150))
rows, cols, channels = addImg.shape
roi = foreground[foreground.shape[0]-rows:foreground.shape[0], foreground.shape[1]-cols:foreground.shape[1]]
result = cv2.addWeighted(roi, 0.2, addImg, 0.8, 0) # 0 為gamma 修正係數
foreground[foreground.shape[0]-rows:foreground.shape[0], foreground.shape[1]-cols:foreground.shape[1]] = result
cv2.imwrite('result2.jpg', foreground)