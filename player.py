from human import Human
from ai import Ai

class Player:

    def __init__(self,player, wins):
        self.player_1 = player
        self.player_2 = player
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.wins = 0

    
    def get_player1_gesture(self, player1_gesture):
        self.player_1_gesture = player1_gesture
        return self.player_1_gesture
    
    def get_player2_gesture(self, player2_gesture):
        self.player_2_gesture = player2_gesture
        return self.player_2_gesture