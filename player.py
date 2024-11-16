class Player:
    def __init__(self, playerX, playerY, actualPosX, actualPosY):
        self.playerX = playerX
        self.playerY = playerY
        self.actualPosX = actualPosX
        self.actualPosY = actualPosY
    
    def getLatLongForClick(self, clickX, clickY):
        # 600 x 800
        propX = clickX / 600
        eqLat = 


        self.actualLat = 