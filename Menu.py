from Player import Player
from Game import Game

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

    def intro_loop(self):
        loop = True
        while loop:
            self.print_menu('Main Menu', 'New Game', 'Open Existing Game', 'Exit')
            choice = input("Enter choice [1-3]: ")
            if(choice == '1'):
                self.new_game_loop()
            elif(choice == '2'):
                file = input("Enter File for Existing Game: ")
            elif(choice == '3'):
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
                print("saving")
                shuff = ""
                while shuff != 'y' and shuff != 'n':
                    shuff = input("Would you like to shuffle players? (y/n)")
                    if(shuff == 'y'):
                        print("Shuffling...")
                        self.game.shuffle_players()
                    elif(shuff != 'n'):
                        print("Invalid input.")
                self.game_edit_loop()
            elif(choice == '6'):
                """ask if save"""
                loop = False
            else:
                print("Invalid Input.")

    def game_edit_loop(self):
        loop = True
        while loop:
            self.print_menu('Edit Game: ' + self.name, 'Register Kill', 'View Alive Players',
            'View Dead Players', 'View Wanted List', 'Add Player to Wanted List', 'Save', 'Back')
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
                if self.game.get_index(wanted_name) is None:
                    print("Can't find player: " + wanted_name)
                    continue
                self.game.players[self.game.get_index(wanted_name)].set_wanted()
            elif(choice == '6'):
                print("saving")
                """ save"""
            elif(choice == '7'):
                """ ask if save"""
                loop = False
            else:
                print("Invalid Input")
