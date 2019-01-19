import datetime
import pytz

class Player:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.death_time = -1
        self.wanted = False
        self.wanted_time = -1

    def print_player(self):
        print('Name: ' + self.name, "Alive: " + str(self.is_alive), "Death Time: " + str(self.death_time),
            "Wanted: " + str(self.wanted), "Wanted Time: " + str(self.wanted_time), sep="\n")

    def set_death(self):
        self.is_alive = False;
        self.death_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
        self.wanted = False
        self.wanted_time = -1

    def set_wanted(self):
        self.wanted = True;
        self.wanted_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
