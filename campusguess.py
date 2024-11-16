from cmu_graphics import *
import requests
import os
import math
from PIL import Image
from PIL.ExifTags import TAGS
from spot import Spot
# spandan


lat = 40.442657
lon = -79.943561
image = Spot(lon,lat,"151.78","-0.76")
image.getImage()
print(image)



# API_KEY = "AIzaSyDjKrXMaHoiZSSQ-_yI-Gl57qytkcoFSKA"
# BASE_URL = "https://maps.googleapis.com/maps/api/streetview"
# params = {
#     "size": "600x300",
#     "location": f"{lat},{lon}",
#     "heading": "151.78",
#     "pitch": "-0.76",
#     "key": API_KEY
# }

# response = requests.get(BASE_URL, params=params)

# if response.status_code == 200:
#     image_filename = "street_view_image.jpg"
#     with open(image_filename, "wb") as file:
#         file.write(response.content)
#     print(f'Street View Image saved as {image_filename}')
# else:
#     print(f'Error: {response.status_code}. Unable to fetch the image.')


# print(response)
# print(type(response))
# # with open("street_view.jpg", "wb") as file:
# #     file.write(response.content)

# image_path = "/Users/hans/Downloads/CMUImages/IMG_1030.JPG"



#get_coordinate gets the long,lait of a image 
# def get_coordinate(image_path):

#     # Open image 
#     image = Image.open(image_path)

#     exif = {}
#     if image._getexif() is not None:
#         for tag, value in image._getexif().items():
#             if tag in TAGS:
#                 exif[TAGS[tag]] = value

#     if "GPSInfo" in exif:
#         gps_info = exif["GPSInfo"]

#         def convert_to_degrees(value):

#             d = float(value[0])
#             m = float(value[1])
#             s = float(value[2])
#             return d + (m / 60.0) + (s / 3600.0)

#         # Convert latitude and longitude to degrees
#         lat = convert_to_degrees(gps_info[2])
#         lon = convert_to_degrees(gps_info[4])
#         lat_ref = gps_info[1]
#         lon_ref = gps_info[3]

#         if lat_ref != "N":
#             lat = -lat
#         if lon_ref != "E":
#             lon = -lon
        

#         geo_coordinate = (lon, lat)

#         return geo_coordinate


# def drawGuessDot(app):
#     if app.click_coordinates:
#         clickX, clickY = app.click_coordinates
#         drawCircle(clickX, clickY, 6, fill='red', border='black')
        
#         targetX, targetY = app.target_dot
#         drawCircle(targetX, targetY, 6, fill='blue', border='black')
        
#         drawLine(clickX, clickY, targetX, targetY, fill='black')
        
# def onAppStart(app):
#     app.coordinates = get_coordinate(image_path)
#     app.click_coordinates = None

# # hi derrick
# # hi
# def redrawAll(app):
#     drawRect(150, 150, 200, 100, fill = None, border = 'black', borderWidth = 5)
#     drawLabel('Start Game', 200, 200, size = 2)

# def onMousePress(app):
#     pass

# def distance(x0, y0, x1, y1):
#     return math.sqrt((x1-x0)**2 + (y1-y0)**2)

# runApp()