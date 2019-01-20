import datetime
import pytz

class Player:
    __last_id = 0
    def __init__(self, name):
        self.id = Player.__last_id;
        self.name = name
        self.is_alive = True
        self.death_time = -1
        self.killer = ""
        self.wanted = False
        self.wanted_time = -1
        """ make kills be list??"""
        self.kills = 0;
        Player.__last_id += 1;

    def print_player(self):
        print('ID: ' + str(self.id), 'Name: ' + self.name, "Alive: " + str(self.is_alive), "Death Time: " + str(self.death_time),
            "Killer: " + self.killer,"Wanted: " + str(self.wanted), "Wanted Time: " + str(self.wanted_time),
            'Kills: ' + str(self.kills), sep="\n")

    def set_death(self, killer):
        self.is_alive = False;
        self.death_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
        self.wanted = False
        self.wanted_time = -1
        self.killer = killer

    def set_wanted(self):
        self.wanted = True;
        self.wanted_time = datetime.datetime.now(pytz.timezone('America/Chicago'))

    def inc_kills(self):
        self.kills += 1
