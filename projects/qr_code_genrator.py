import pyqrcode


def qr_code_generator():
    data = input("Enter Data you want to save in QR code : ")
    url = pyqrcode.create(data)
    url.png("../demo_img/" + input("Enter name for QRCODE: ") + ".png", scale=6)


qr_code_generator()