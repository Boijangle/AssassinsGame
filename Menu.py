from Player import Player
from Game import Game

class Menu:
    def __init__(self):
        self.game = None
        self.name = "";

    def intro_menu(self):
        print('-' * 30, "Main Menu", '-' * 30)
        print("1. New Game")
        print("2. Open Existing Game")
        print("3. Exit")
        print('-' * 71)

    def new_menu(self):
        print('-' * 30, "New Game: " + self.name, '-' * 30)
        print("1. Add Player")
        print("2. Remove Player")
        print("3. View All Players")
        print("4. Save and Start")
        print("5. Back")
        print('-' * (72 + len(self.name)))

    def game_edit_menu(self):
        print('-' * 30, "Edit Game: " + self.name, '-' * 30)
        print("1. Register Kill")
        print("2. View Alive Players")
        print("3. View Dead Players")
        print("4. View Wanted List")
        print("5. Add Player to Wanted List")
        print("6. Save")
        print("7. Back")
        print('-' * (73 + len(self.name)))

    def intro_loop(self):
        loop = True
        while loop:
            self.intro_menu()
            choice = int(input("Enter choice [1-3]: "))
            if(choice == 1):
                self.new_game_loop()
            elif(choice == 2):
                file = input("Enter File for Existing Game: ")
            elif(choice == 3):
                loop = False
                return loop
                print("Quitting...")
            else:
                print("Invalid Input.")

    def new_game_loop(self):
        self.game = Game()
        self.name = input("Enter Name for New Game: ")
        loop = True
        while loop:
            self.new_menu()
            choice = int(input("Enter choice [1-5]: "))
            if(choice == 1):
                player_name = input("Player Name: ")
                self.game.add_player(player_name)
            elif(choice == 2):
                player_name = input("Player Name: ")
                self.game.remove_player(player_name)
            elif(choice == 3):
                print("Current Players: ")
                self.game.print_players()
            elif(choice == 4):
                print("saving")
                """ ask to randomize order """
                self.game_edit_loop()
            elif(choice == 5):
                """ask if save"""
                loop = False
            else:
                print("Invalid Input.")

    def game_edit_loop(self):
        loop = True
        while loop:
            self.game_edit_menu()
            choice = int(input("Enter choice [1-6]: "))
            if(choice == 1):
                killer = input("Killer: ")
                victim = input("Victim: ")
                self.game.attempt_kill(killer, victim)
            elif(choice == 2):
                print("Alive Players: ")
                self.game.print_players()
            elif(choice == 3):
                print("Dead Players: ")
                self.game.print_dead_players()
            elif(choice == 4):
                print("Wanted List: ")
                """print wanted list"""
            elif(choice == 5):
                wanted_name = input("Player name to add: ")
                """wanted logic"""
            elif(choice == 6):
                print("saving")
                """ save"""
            elif(choice == 7):
                """ ask if save"""
                loop = False
            else:
                print("Invalid Input")
