import datetime, pytz

class Player:
    __last_id = 0

    def __init__(self, name, id = -1, alive = True, death_time = -1,
    killer = "", wanted = False, wanted_time = -1, kills = None):
        self.id = id
        if(id == -1):
            self.id = Player.__last_id
        self.name = name
        self.alive = alive
        self.death_time = death_time
        self.killer = killer
        self.wanted = wanted
        self.wanted_time = wanted_time
        self.kills = kills
        if(kills is None):
            self.kills = []
        Player.__last_id += 1;

    def print_player(self):
        print('ID: ' + str(self.id), 'Name: ' + self.name, "Alive: " + str(self.alive), "Death Time: " + str(self.death_time),
            "Killer: " + self.killer,"Wanted: " + str(self.wanted), "Wanted Time: " + str(self.wanted_time),
            'Kills: ' + ', '.join(self.kills), sep="\n")

    def get_name(self):
        return self.name

    def set_death(self, killer):
        self.alive = False
        self.death_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
        self.wanted = False
        self.wanted_time = -1
        self.killer = killer

    def force_death(self):
            self.alive = False
            self.death_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
            self.wanted = False
            self.wanted_time = -1
            self.killer = "Forced Death"

    def set_wanted(self):
        self.wanted = True
        self.wanted_time = datetime.datetime.now(pytz.timezone('America/Chicago'))

    def remove_wanted(self):
        self.wanted = False
        self.wanted_time = -1

    def add_kill(self, victim):
        self.kills.append(victim)

    def is_wanted(self):
        return self.wanted

    def is_alive(self):
        return self.alive
