# Assignment 10
# Contact Tracing App
# Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file 
#   - including the date and time it was readimport cv2

import cv2
import pyzbar.pyzbar as pyzbar

# function to read QR Code
def readQRc(frame):
    # decoding QR from webcam
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        x, y , w, h = qrcode.rect
        
        # drawing rectangle to see if code is detected
        qrcodeInfo = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 0), 2)
        
        # text to show decoded data
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, qrcodeInfo, (x + 6, y - 6), font, 1.0, (0, 0, 255), 3)

        # writing it into a text file
        with open("QRinfo.txt", mode ='w') as file:
            file.write("Scanned QR Code:" + qrcodeInfo)
    return frame

def read():

    # initializing web cam 
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()

    # loop to continuously scan for QR and not close
    while ret:
        ret, frame = webcam.read()
        frame = readQRc(frame)
        cv2.imshow('QR Code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # closing webcam
    webcam.release()
    cv2.destroyAllWindows()

read()