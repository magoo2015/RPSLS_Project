from human import Human
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

         print("""\n\nHere are the gesture conditions:\n\n
         Scissors cut Paper
         Paper covers Rock
         Lizard poisons Spock
         Spock smashes scissors
         Scissors decapitates Lizard
         Lizard eats Paper
         Paper disproves Spock
         Spock vaporizes Rock
         Rock crushes Scissors
         """)
    

    def choose_players(self):
       
        pass


    def human_ai(self):
        pass

    #maybe just a human and ai method?
    def human_human(self):
        self.player_1 = Human("Player 1", 0)
        self.player_2 = Human("Player 2", 0)
        pass


    def ai_ai(self):
        pass

    def play_game():

 

    def start_game(self):
        self.display_welcome()
        self.display_rules()
