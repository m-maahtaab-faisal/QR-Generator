import qrcode
url = input("Enter the URL you want to make QR Code: ")
filename = input("Enter Your File Name: ")
file = f"{filename}.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file)
print("QR Was Generated.")