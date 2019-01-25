from Player import Player
from random import shuffle
class Game:

    def __init__(self):
        self.players = []
        self.dead_players = []

    def shuffle_players(self):
        shuffle(self.players)

    def add_player(self, player_name):
        player = Player(player_name)
        self.players.append(player)
        print("Added " + player_name)

    def remove_player(self, player_name):
        ndx = self.get_index(player_name)
        if(ndx is not None):
            del self.players[ndx]
            print("Removed " + player_name)
        else:
            print("Can't find player: " + player_name)

    def print_players(self):
        for x in self.players:
            x.print_player()
            print("\n")

    def print_dead_players(self):
        for x in self.dead_players:
            x.print_player()
            print("\n")

    def print_wanted_list(self):
        for x in self.players:
            if x.is_wanted():
                x.print_player()
                print("\n")

    def get_index(self, name):
        gen = (i for i,x in enumerate(self.players) if x.name == name)
        for i in gen: return i

    def attempt_kill(self, killer_name, victim_name):
        # get killer and victim index
        killer_ndx = self.get_index(killer_name)
        victim_ndx = self.get_index(victim_name)

        # check if both the killer and victim were found
        if killer_ndx is None or victim_ndx is None:
            if killer_ndx is None:
                print("Can't find killer: " + killer_name)
            if victim_ndx is None:
                print("Can't find victim: " + victim_name)
            return

        # check if killer hit direct target, their assassin, or target was on wanted list
        if((killer_ndx + 1) % len(self.players) == victim_ndx
        or (killer_ndx - 1) % len(self.players) == victim_ndx
        or self.players[victim_ndx].is_wanted()):
            # add to kill list
            self.players[killer_ndx].add_kill(victim_name)
            # set victim to dead state
            self.players[victim_ndx].set_death(killer_name)
            # remove victim from live list and add to dead list
            self.dead_players.append(self.players.pop(victim_ndx))
            print("kill confirmed, " + victim_name + " is dead")
        else:
            # if kill was bad, put killer on wanted list
            print("invalid kill " + killer_name + " is on wanted list")
            self.players[killer_ndx].set_wanted()
