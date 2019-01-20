class Game:

    def __init__(self):
        self.players = []
        self.dead_players = []

    def add_players(self, player):
        self.players.append(player)

    def print_players(self):
        for x in self.players:
            x.print_player()
            print("\n")

    def print_dead_players(self):
        for x in self.dead_players:
            x.print_player()
            print("\n")

    def get_index(self, name):
        gen = (i for i,x in enumerate(self.players) if x.name == name)
        for i in gen: return i

    def attempt_kill(self, killer, victim):
        """ finish kill logic """
        """ add wanted list functionality and penalties for bad kills """
        # get killer and victim index
        kill_ndx = self.get_index(killer)
        victim_ndx = self.get_index(victim)

        # check if killer hit direct target or their assassin
        if((kill_ndx + 1) % len(self.players) == victim_ndx
        or (kill_ndx - 1) % len(self.players) == victim_ndx):
            # increase num kills
            self.players[kill_ndx].inc_kills()
            # set victim to dead state
            self.players[victim_ndx].set_death(killer)
            # remove victim from live list and add to dead list
            self.dead_players.append(self.players.pop(victim_ndx))
            print("kill confirmed")
        else:
            print("kill failed")
