"""
Script to experiment with QR code generation

Further ideas:
instrumentation labels - adds description, sensor, ... everything
random surveys around city
product info
linkliker

"""

# necessary imports
import qrcode
from PIL import Image

# create qr data stuff
qrd = "This is how I will store all my information"

# create the qr code
qr = qrcode.make(qrd)

# save as png...
qr.save("qri.png")

# END
