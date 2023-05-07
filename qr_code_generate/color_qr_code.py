import qrcode
myQrCode = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
myQrCode.add_data('hi!  how are you')
myQrCode.make(fit=True)          # 根據參數製作為 QRCode 物件
img = myQrCode.make_image(fill_color="#ff0000", back_color="#ffffff")      # 產生 QRCode 圖片
img.show()        