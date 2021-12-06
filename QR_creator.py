#Coded by Daniyal Arteshdar (Py.Dan)
import qrcode

# Enter your link
data = "https://www.nasa.gov/"

# QR Sizing
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

qr.add_data(data)
qr.make(fit=True)

# QR personalization
img = qr.make_image(fill_color='black',
                    back_color='white')

# Save it as PNG file in directory
img.save('MyQR.png')
