from cmu_graphics import *
from PIL import Image
from PIL.ExifTags import TAGS
from spot import Spot
# spandan


lon = 40728.444646
lat = -79.942992
image = Spot(lon,lat,0,-0.76)
image.getImage()

print(image)