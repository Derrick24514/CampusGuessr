class leaderboardEntry:
    def __init__(self,name,highscore):
        self.name = name
        self.highscore = highscore

    def __repr__(self):
        return f'{self.name} - {self.highscore}'
    
    def __lt__(self,other):
        return self.highscore < other.highscore
    
    def __gt__(self,other):
        return self.highscore > other.highscore
    
    def __eq__(self,other):
        return self.highscore == other.highscore