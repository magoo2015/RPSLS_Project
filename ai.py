from players import Player
import random
import time

class Ai(Player):
    
    def __init__(self, name):
        super().__init__(name,)
        
        pass

    def get_gestures(self):
        self.choice = random.randint(0, 4)
        print("")
        print(f"{self.player} chose {self.gestures[self.choice]}")
        print("")
        time.sleep(2)
        return self.choice

    