


class Player:

    def __init__(self,player, wins):
        self.player = player
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.wins = wins

    
    def get_player1_gesture(self, player1_gesture):
        self.player_1_gesture = player1_gesture
        return self.player_1_gesture
    
    def get_player2_gesture(self, player2_gesture):
        self.player_2_gesture = player2_gesture
        return self.player_2_gesture