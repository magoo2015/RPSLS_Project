from unicodedata import name
from players import Player
import time

class Human(Player):
    def __init__(self, players, wins):
        super().__init__(players, wins)
        
        
        


    
    def get_gestures(self):
        print("""
        Choose 0 for Rock.
        Choose 1 for Paper.
        Choose 2 for Scissors.
        Choose 3 for Lizard.
        Choose 4 for Spock.
        """)
        self.choice = int(input("Choose your gesture. "))
        print("")
        if self.choice not in range(0, 5):
            print("Invalid choice, please choose again")
            self.get_gestures()
        elif self.choice in range(0, 5):
            print(f"{self.player} chose {self.gestures[self.choice]}")
            time.sleep(2)
        #return self.gestures
        

    