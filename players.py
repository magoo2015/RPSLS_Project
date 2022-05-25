


class Player:

    def __init__(self,player, wins):
        self.player = player
        self.gestures = []
        self.wins = wins

    
    def get_gestures(self):
        self.gestures = input("Choose your gesture.")
        return self.gestures