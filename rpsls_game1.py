from players import Player





class Rpsls_game:

    def __init__(self):
        self.player_1 = Player("Player 1", 0)
        self.player_2 = Player("Player 2", 0)
        self.AI_1 = Player("AI_one", 0)
        self.AI_2 = Player("AI_two", 0)


    def display_welcome(self):
        print("""
        **********************************************
        Welcome to Rock Paper Scissors Lizard Spock!!!
        **********************************************
        """)
       

    def display_rules(self):
         print("Each game will be the best of three games")
         print("Use the number keys to make your selection.\n\n")

         print("\n\nHere are the gesture conditions:\n\nScissors cut Paper\nPaper covers Rock\nLizard poisons Spock\nSpock smashes scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")



    def rpsls_game(self, player_1, player_2):
        gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        

        pass

    def one_player(self):




    def start_game(self):
        self.display_welcome()
        self.display_rules()
