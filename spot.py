from cmu_graphics import *
import requests
import os
import math
from PIL import Image
from PIL.ExifTags import TAGS

class Spot:
    def __init__(self, long, lat, heading, pitch):
        self.longitude = long
        self.latitude = lat
        self.heading = heading
        self.pitch = pitch

    def __repr__(self):
        return f'Longitude of {self.longitude}, latitude of {self.latitude}, heading of {self.heading}, and pitch of {self.pitch}'
    
    def changeHeadingRight(self):
        self.heading += 10
    
    def changeHeadingLeft(self):
        self.heading -= 10
    
    def changePitchUp(self):
        self.pitch += 10
    
    def changePitchDown(self):
        self.pitch -= 10
    
    def getImage(self):
        API_KEY = "AIzaSyDjKrXMaHoiZSSQ-_yI-Gl57qytkcoFSKA"
        BASE_URL = "https://maps.googleapis.com/maps/api/streetview"
        params = {
            "size": "600x300",
            "location": f'{self.latitude},{self.longitude}',
            "heading": f'{self.heading}',
            "pitch": f'{self.pitch}',
            "key": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        print(response.content)
        print(response.status_code)
        if response.status_code == 200:
            image_filename = "street_view_image.jpg"
            with open(image_filename, "wb") as file:
                file.write(response.content)
                print(f'Street View Image saved as {image_filename}')
        elif response.status_code == 204:
            print('No Image Found')
        else:
            print(f'Error: {response.status_code}. Unable to fetch the image.')

        print(response)
        print(type(response))
    # with open("street_view.jpg", "wb") as file:
    #     file.write(response.content)

    def moveView(self):
        pass