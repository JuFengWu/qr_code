import cv2 
from pyzbar.pyzbar import decode

img = cv2.imread("qrcode.png")

x = decode(img)
print(x)
print(x[0].data)