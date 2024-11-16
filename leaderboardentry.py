class leaderboardEntry:
    def __init__(self,name,highscore):
        self.name = name
        self.highscore = highscore

    def __repr__(self):
        return f'{self.name} - {self.highscore}'