import qrcode

with open('contact_details.txt') as txt:
    details = txt.read()

qr = qrcode.make(details)
qr.save('myQRCode.png')
