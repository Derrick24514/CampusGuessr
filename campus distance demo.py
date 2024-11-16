from cmu_graphics import *
from PIL import Image
from PIL.ExifTags import TAGS
import os
import math
import pyproj

def get_coordinate(image_path):

    image = Image.open(image_path)

    exif = {}
    if image._getexif() is not None:
        for tag, value in image._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]] = value

    if "GPSInfo" in exif:
        gps_info = exif["GPSInfo"]

        def convert_to_degrees(value):
            d = float(value[0])
            m = float(value[1])
            s = float(value[2])
            return d + (m / 60.0) + (s / 3600.0)

        # Convert latitude and longitude to degrees
        lat = convert_to_degrees(gps_info[2])
        lon = convert_to_degrees(gps_info[4])
        lat_ref = gps_info[1]
        lon_ref = gps_info[3]

        if lat_ref != "N":
            lat = -lat
        if lon_ref != "E":
            lon = -lon

        geo_coordinate = (lon, lat)
        return geo_coordinate

def geo_to_screen(lon, lat, width, height):
    # Convert lat/lon to screen space using Mercator projection
    project = pyproj.Transformer.from_proj(
        proj_from=pyproj.Proj("epsg:4326"),  # WGS84 coordinate system
        proj_to=pyproj.Proj("epsg:3857")     # Web Mercator projection
    ).transform

    mercator_x, mercator_y = project(lat, lon)
    screen_x = int((mercator_x + 20037508.34) * (width / 40075016.68))
    screen_y = int((20037508.34 - mercator_y) * (height / 40075016.68))
    return screen_x, screen_y

def screen_to_geo(screen_x, screen_y, width, height):
    # Convert screen space back to lat/lon using Mercator projection
    inverse_project = pyproj.Transformer.from_proj(
        proj_from=pyproj.Proj("epsg:3857"),  # Web Mercator projection
        proj_to=pyproj.Proj("epsg:4326")     # WGS84 coordinate system
    ).transform

    mercator_x = screen_x * (40075016.68 / width) - 20037508.34
    mercator_y = 20037508.34 - screen_y * (40075016.68 / height)
    lon, lat = inverse_project(mercator_y, mercator_x)
    lat = max(min(lat, 90), -90)
    return lon, lat

def loadPilImage(filePath):
    return Image.open(filePath)

def onAppStart(app):
    app.width=900
    app.height=700
    setupCmuMap(app)
    lat = 41
    lon = -79.940990
    app.coordinates = (lat,lon)
    app.coordx=app.coordinates[0]
    app.coordy=-app.coordinates[1]
    app.click_coordinates = None
    app.target_dot= geo_to_screen(app.coordx,app.coordy,app.imageWidth//2,app.imageHeight//2)
    app.target_dot=(app.target_dot[0]-100,app.target_dot[1]+350)

def setupCmuMap(app):
    app.cmufilePath ='/Users/kurtschimmel/Desktop/cmuguess/campusguess/Screenshot 2024-11-15 at 9.32.48 PM.jpeg'
    cmupilImage = loadPilImage(app.cmufilePath)

    app.imageWidth, app.imageHeight = cmupilImage.size
    cmupilImage = cmupilImage.resize((app.imageWidth//2, app.imageHeight//2))

    app.cmuImage = CMUImage(cmupilImage)



def redrawAll(app):
    drawImage(app.cmuImage, 0, 0)
    drawGuessDot(app)

def drawGuessDot(app):
    if app.click_coordinates:
        clickX, clickY = app.click_coordinates
        drawCircle(clickX, clickY, 6, fill='red', border='black')
        
        targetX, targetY = app.target_dot
        drawCircle(targetX, targetY, 6, fill='blue', border='black')
        
        drawLine(clickX, clickY, targetX, targetY, fill='black')
    
    drawRect(0,600,200,84,fill='green')

def onMousePress(app,mouseX,mouseY):
    app.click_coordinates=mouseX,mouseY


runApp()
