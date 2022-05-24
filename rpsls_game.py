from player import Player





class Rpsls_game:

    def __init__(self):
        self.player_1 = Player("Player 1")
        self.player_2 = Player("Player 2")
        self.AI_1 = Player("AI_one")
        self.AI_2 = Player("AI_two")


    def display_welcome(self):
        print("""
        **********************************************
        Welcome to Rock Paper Scissors Lizard Spock!!!
        **********************************************
        """)
       

    def display_rules(self):
         print("Each game will be the best of three games")

         print("\n\nHere are the gesture conditions:\n\nScissors cut Paper\nPaper covers Rock\nLizard poisons Spock\nSpock smashes scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")



    def rpsls_game(self, player_1, player_2):
        self.player_1.gestures
        pass



    def start_game(self):
        self.display_welcome()
        self.display_rules
