from Game import Game
from random import shuffle
import sys

class Menu:
    def __init__(self):
        self.game = None
        self.name = "";

    def print_menu(self, title, *args):
        print('-' * 30, title, '-' * 30)
        x = 1
        for op in args:
            print(str(x) + ". " + op)
            x += 1
        print('-' * (62 + len(title)))

    def save_diag(self):
        print("Saving...")
        sav = ""
        while sav != 'y' and sav != 'n':
            sav = input("Would you like to save? (y/n)")
            if(sav == 'y'):
                print("Saving...")
                self.game.save_csv(self.name)
            elif(sav != 'n'):
                print("Invalid input.")

    def shuff_diag(self):
        shuff = ""
        while shuff != 'y' and shuff != 'n':
            shuff = input("Would you like to shuffle players? (y/n)")
            if(shuff == 'y'):
                print("Shuffling...")
                self.game.shuffle_players()
            elif(shuff != 'n'):
                print("Invalid input.")

    def quit_diag(self):
        self.save_diag()
        print("Quitting...")
        sys.exit(0)

    def intro_loop(self):
        self.game = Game()
        loop = True
        while loop:
            self.print_menu('Main Menu', 'New Game', 'Open Existing Game', 'Exit')
            choice = input("Enter choice [1-3]: ")
            if(choice == '1'):
                self.game = Game()
                self.new_game_loop()
            elif(choice == '2'):
                self.game = Game()
                file = input("Enter File for Existing Game: ")
                self.game.load_csv(file)
                self.name = file
                self.game_edit_loop()
            elif(choice == '3'):
                self.quit_diag()
            else:
                print("Invalid Input.")

    def new_game_loop(self):
        self.name = input("Enter Name for New Game: ")
        loop = True
        while loop:
            self.print_menu('New Game: ' + self.name, 'Add Player', 'Remove Player',
            'View All Players', 'Shuffle Players', 'Save and Start', 'Back')
            choice = input("Enter choice [1-5]: ")
            if(choice == '1'):
                player_name = input("Player Name: ")
                self.game.add_player(player_name)
            elif(choice == '2'):
                player_name = input("Player Name: ")
                self.game.remove_player(player_name)
            elif(choice == '3'):
                print("Current Players: \n")
                self.game.print_players()
            elif(choice == '4'):
                print("Shuffling...")
                self.game.shuffle_players()
            elif(choice == '5'):
                self.shuff_diag()
                print("Saving...")
                self.game.save_csv(self.name)
                self.game_edit_loop()
            elif(choice == '6'):
                self.save_diag()
                loop = False
            elif(choice == 'q'):
                self.quit_diag()
            else:
                print("Invalid Input.")

    def game_edit_loop(self):
        loop = True
        #self.game.check_wanted()
        while loop:
            self.print_menu('Edit Game: ' + self.name, 'Register Kill', 'View Alive Players',
            'View Dead Players', 'View Wanted List', 'Add Player to Wanted List', 'Remove Player from Wanted List',
            'Update Wanted List', 'Save', 'Back')
            choice = input("Enter choice [1-6]: ")
            if(choice == '1'):
                killer = input("Killer: ")
                victim = input("Victim: ")
                self.game.attempt_kill(killer, victim)
            elif(choice == '2'):
                print("Alive Players: \n")
                self.game.print_players()
            elif(choice == '3'):
                print("Dead Players: \n")
                self.game.print_dead_players()
            elif(choice == '4'):
                print("Wanted List: \n")
                self.game.print_wanted_list()
            elif(choice == '5'):
                wanted_name = input("Player name to add: ")
                self.game.add_wanted(wanted_name)
            elif(choice == '6'):
                remove_name = input("Player name to remove: ")
                self.game.remove_wanted(remove_name)
            elif(choice == '7'):
                self.game.check_wanted()
            elif(choice == '8'):
                print("Saving...")
                self.game.save_csv(self.name)
            elif(choice == '9'):
                self.save_diag()
                loop = False
            elif(choice == 'q'):
                self.quit_diag()
            else:
                print("Invalid Input")
