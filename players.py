


class Player:

    def __init__(self,player, wins):
        self.player = player
        self.gestures = []
        self.wins = wins

    
    def get_gestures(self):
        print("""
        Choose 0 for Rock.
        Choose 1 for Paper.
        Choose 2 for Scissors.
        Choose 3 for Lizard.
        Choose 4 for Spock.
        """)
        self.gestures = int(input("Choose your gesture. "))
        return self.gestures