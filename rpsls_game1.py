from ai import Ai
from human import Human
from players import Player
import time





class Rpsls_game:

    def __init__(self):
        self.player_1 = Player("Player 1", 0)
        self.player_2 = Player("Player 2", 0)
        self.AI_1 = Player("AI_one", 0)
        self.AI_2 = Player("AI_two", 0)
        self.num_of_players = 0
        self.player = ""
        self.ai = ""



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

        self.num_of_players = int(input("How many players? Choose 1, 2, or 3 for AI vs AI ! "))

        if self.num_of_players not in range(1, 4):
            print("This is not a vailid choose, please try again.")
            self.choose_players()
        elif self.num_of_players == 1:
            return self.human_vs_ai()
        elif self.num_of_players == 2:
            return self.human_vs_human()
        elif self.num_of_players == 3:
            return self.ai_vs_ai()

    def human_vs_ai(self):
        time.sleep(1)
        self.player_1 = Human("Player 1", 0)
        self.AI_1 = Ai("Ai", 0)
        game_on = True
        

        while game_on:

            self.player_1.get_gestures()
            self.AI_1.ai_gestures()
            if self.player_1.gestures == self.AI_1.gestures:
                print("It's a tie!")
            elif self.player_1.gestures == 0 and self.AI_1.gestures == 1:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 0 and self.AI_1.gestures == 4:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 1 and self.AI_1.gestures == 2:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 1 and self.AI_1.gestures == 3:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 2 and self.AI_1.gestures == 0:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 2 and self.AI_1.gestures == 4:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 3 and self.AI_1.gestures == 0:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 3 and self.AI_1.gestures == 2:
                print("You lose!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 4 and self.AI_1.gestures == 1:
                print("You lose")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 4 and self.AI_1.gestures == 3:
                print("You lose")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("AI wins the game!")
                    game_on = False
                    self.end_game()
            else:
                print("You win!")
                self.player_1.wins += 1
                if self.player_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_1.wins >= 2:
                    print("Player 1 wins the game!")
                    game_on = False
                    self.end_game()



    
    def human_vs_human(self):
        time.sleep(1)
        self.player_1 = Human("Player 1", 0)
        self.player_2 = Human("Player 2",0)
        game_on = True
        

        while game_on:

            self.player_1.get_gestures()
            self.player_2.get_gestures()
            if self.player_1.gestures == self.player_2.gestures:
                print("It's a tie!")
            elif self.player_1.gestures == 0 and self.player_2.gestures == 1:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 0 and self.player_2.gestures == 4:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 1 and self.player_2.gestures == 2:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 1 and self.player_2.gestures == 3:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 2 and self.player_2.gestures == 0:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins<= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 2 and self.player_2.gestures == 4:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 3 and self.player_2.gestures == 0:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 3 and self.player_2.gestures == 2:
                print("You lose!")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 4 and self.player_2.gestures == 1:
                print("You lose")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.player_1.gestures == 4 and self.player_2.gestures == 3:
                print("You lose")
                self.player_2.wins += 1
                if self.player_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Player 2 wins the game!")
                    game_on = False
                    self.end_game()
            else:
                print("You win!")
                self.player_1.wins += 1
                if self.player_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_1.wins >= 2:
                    print("Player 1 wins the game!")
                    game_on = False
                    self.end_game()

    def ai_vs_ai(self):
        time.sleep(1)
        self.AI_1 = Ai("Ai 1", 0)
        self.AI_2 = Ai("Ai 2", 0)
        game_on = True
        

        while game_on:

            self.AI_1.ai_gestures()
            self.AI_2.ai_gestures()
            if self.AI_1.gestures == self.AI_2.gestures:
                print("It's a tie!")
            elif self.AI_1.gestures == 0 and self.AI_2.gestures == 1:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 0 and self.AI_2.gestures == 4:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 1 and self.AI_2.gestures == 2:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 1 and self.AI_2.gestures == 3:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 2 and self.AI_2.gestures == 0:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 2 and self.AI_2.gestures == 4:
                print("Ai loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 3 and self.AI_2.gestures == 0:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 3 and self.AI_2.gestures == 2:
                print("Ai 1 loses!")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.player_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 4 and self.AI_2.gestures == 1:
                print("Ai 1 loses")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("AI 2 wins the game!")
                    game_on = False
                    self.end_game()
            elif self.AI_1.gestures == 4 and self.AI_2.gestures == 3:
                print("Ai 1 loses")
                self.AI_2.wins += 1
                if self.AI_2.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    game_on = True
                elif self.AI_2.wins >= 2:
                    print("Ai 2 wins the game!")
                    game_on = False
                    self.end_game()
            else:
                print("Ai 2 loses!")
                self.AI_1.wins += 1
                if self.AI_1.wins <= 1:
                    print("Time for round 2, first to two wins is the winner!")
                    time.sleep(2)
                    game_on = True
                elif self.AI_1.wins >= 2:
                    print("Ai 1 wins the game!")
                    game_on = False
                    self.end_game()

    
    def end_game(self):
        time.sleep(2)
        print("")
        print("Game Over!")
        
            
        
    def start_game(self):
        self.display_welcome()
        time.sleep(2)
        self.display_rules()
        time.sleep(2)
        self.choose_players()
        
