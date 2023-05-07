

import qrcode
img = qrcode.make('hi!  how are you')    # 要轉換成 QRCode 的文字或是網站
img.show()                
img.save('qrcode.png')    
 