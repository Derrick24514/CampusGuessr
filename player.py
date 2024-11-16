import math

class Player:
    def __init__(self, playerX, playerY, actualLat, actualLong):
        self.playerX = playerX
        self.playerY = playerY
        self.actualPosX = actualLat
        self.actualPosY = actualLong
        self.convertedLat = 0
        self.convertedLong = 0
        self.distance = 0
        self.score = 0
    
    def getLatLongForClick(self):
        # 600 x 800
        boardLength = 800
        boardHeight = 600
        propX = self.playerX / boardLength
        propY = self.playerY / boardHeight
        self.convertedLat = (propX * (40.440118 - 40.448876)) + 40.448876
        self.convertedLong = (propY * (-79.937617 + 79.951906)) - 79.951906
        return self.convertedLat, self.convertedLong
    

    def haversine(self, lat1, lon1, lat2, lon2):
        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Radius of Earth in kilometers
        R = 6371.0

        # Calculate the distance
        self.distance = R * c *3280.84
        return self.distance

    def scoring(self):
        maxScore = 5000
        actualScore = 5000
        if self.distance == 0:
            self.score = maxScore
        else:
            actualScore = 5000 - (0.1 * self.distance)
            if actualScore < 0:
                self.score = 0

        return self.score 

    
newPlayer = Player(435, 427, 1, 2)
newPlayer2 = Player(492, 282, 1, 2)
print(newPlayer.getLatLongForClick())
print(newPlayer2.getLatLongForClick())

