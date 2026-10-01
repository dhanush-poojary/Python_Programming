import qrcode

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjmMjRY2hxr09wgc4iXfHXSoGyTbsqM_KZXj3xfNLvch_eU8hHHN2ZQwM&s=10"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make()

img = qr.make_image()
img.save("Basics/QRCode/image_qr.png")