from players import Player
import random
import time

class Ai(Player):
    
    def __init__(self):
        super().__init__("AI", 0)
        pass

    def get_gestures(self):
        self.gestures = random.randint(0, 4)
        print("")
        print(f"{self.player} chose {self.choice[self.gestures]}")
        print("")
        time.sleep(2)
        return self.gestures

    