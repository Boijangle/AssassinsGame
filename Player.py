import datetime
import pytz

class Player:
    __last_id = 0
    def __init__(self, name):
        self.id = Player.__last_id;
        self.name = name
        self.alive = True
        self.death_time = -1
        self.killer = ""
        self.wanted = False
        """ do something with this like take them off wanted list"""
        self.wanted_time = -1
        self.kills = [];
        Player.__last_id += 1;

    def print_player(self):
        print('ID: ' + str(self.id), 'Name: ' + self.name, "Alive: " + str(self.alive), "Death Time: " + str(self.death_time),
            "Killer: " + self.killer,"Wanted: " + str(self.wanted), "Wanted Time: " + str(self.wanted_time),
            'Kills: ' + ', '.join(self.kills), sep="\n")

    def get_name(self):
        return self.name

    def set_death(self, killer):
        self.alive = False;
        self.death_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
        self.wanted = False
        self.wanted_time = -1
        self.killer = killer

    def force_death(self):
            self.alive = False;
            self.death_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
            self.wanted = False
            self.wanted_time = -1
            self.killer = "Forced Death"

    def set_wanted(self):
        self.wanted = True;
        self.wanted_time = datetime.datetime.now(pytz.timezone('America/Chicago'))

    def add_kill(self, victim):
        self.kills.append(victim)

    def is_wanted(self):
        return self.wanted
