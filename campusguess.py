from cmu_graphics import *
from PIL import Image
from PIL.ExifTags import TAGS
from spot import Spot
# spandan


lat = 40.442657
lon = -79.943561
image = Spot(lon,lat,0,-0.76)
image.getImage()

print(image)