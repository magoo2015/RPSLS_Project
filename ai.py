from players import Player
import random

class Ai(Player):
    
    def __init__(self, player, wins):
        super().__init__(player, wins)
        pass

    def ai_gestures(self):
        self.gestures = random.randint(0, 4)
        print("")
        print(f"{self.player} chose {self.choice[self.gestures]}")
        print("")
        return self.gestures

    