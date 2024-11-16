class Image:
    def __init__(self, long, lat, heading, pitch):
        self.longitude = long
        self.latitude = lat
        self.heading = heading
        self.pitch = pitch
    
    def changeHeading(self, changeInHeading):
        self.heading += changeInHeading
    
    def changePitch(self, changeInPitch):
        self.pitch += changeInPitch
    
    

