import cv2 
from pyzbar.pyzbar import decode

img = cv2.imread("qrcode.png")

x = decode(img)
print(x)
readData = x[0].data
print(readData)

readData= "文字是" + readData.decode("utf-8") 
print(readData)
