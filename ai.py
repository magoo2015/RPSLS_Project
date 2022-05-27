from players import Player
import random
import time

class Ai(Player):
    
    def __init__(self, players, wins):
        super().__init__(players, wins)
        self.player = players
        self.wins = wins
        pass

    def get_gestures(self):
        self.gestures = random.randint(0, 4)
        print("")
        print(f"{self.player} chose {self.choice[self.gestures]}")
        print("")
        time.sleep(2)
        return self.gestures

    