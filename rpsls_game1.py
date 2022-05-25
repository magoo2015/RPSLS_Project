from ai import Ai
from human import Human
from players import Player





class Rpsls_game:

    def __init__(self):
        self.player_1 = Player("Player 1", 0)
        #self.player_2 = Player("Player 2", 0)
        self.AI_1 = Player("AI_one", 0)
        #self.AI_2 = Player("AI_two", 0)
        self.num_of_players = 0


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
       self.num_of_players = input("How many players? ")
       return self.num_of_players

        

    def human_ai(self):
        pass

    #maybe just a human and ai method?
    def human_human(self, player):
        self.player_1 = player
        pass


    def ai_ai(self, player):
        self.AI_1 = player
        pass

    def play_game(self):
        self.num_of_players = input("How many players? ")
        print(type(self.num_of_players))
        

        if self.num_of_players == "0":
            self.player_1 = Human("Player1", 0)
            self.AI_1 = Ai("Ai", 0)
            print(self.player_1.wins)
            print(self.AI_1.wins)
        elif self.num_of_players == "1":
            self.player_1 = Human("Player1", 0)
            self.player_1 = Human("Player2",0)
            print(self.player_1.wins)



 

    def start_game(self):
        self.display_welcome()
        self.display_rules()
        #self.choose_players()
        self.play_game()
