import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://www.facebook.com/fukuro.art.tech')
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path='Logo.jpg')
img.save('qrcode.png')