from Player import Player
from dateutil.parser import parse
from random import shuffle
import csv, datetime, pytz

class Game:

    def __init__(self):
        self.players = []
        self.dead_players = []

    def shuffle_players(self):
        shuffle(self.players)

    def add_player(self, player_name):
        valid = True
        for x in self.players:
            if x.name == player_name:
                valid = False
        if(valid):
            player = Player(player_name)
            self.players.append(player)
            print("Added " + player_name)
        else:
            print("Player name is already taken")

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

    def get_target(self, name):
        prev_ndx = self.get_index(name)
        if prev_ndx is None:
            print("Can't find player: " + name)
            return -1
        else:
            ndx = (prev_ndx + 1) % len(self.players)
            return self.players[ndx]

    def get_assassin(self, name):
        prev_ndx = self.get_index(name)
        if prev_ndx is None:
            print("Can't find player: " + name)
            return -1
        else:
            ndx = (prev_ndx - 1) % len(self.players)
            return self.players[ndx]

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
            return -1

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
            return 0
        else:
            # if kill was bad, put killer on wanted list
            print("invalid kill " + killer_name + " is on wanted list")
            self.players[killer_ndx].set_wanted()
            return 1

    def check_wanted(self):
        td = datetime.timedelta(days = 1)
        now = datetime.datetime.now(pytz.timezone('America/Chicago'))
        print("Updated Players: \n")
        for p in self.players:
            if p.is_wanted():
                if now - p.wanted_time >= td:
                    p.remove_wanted()

    def remove_wanted(self, name):
        ndx = self.get_index(name)
        if ndx is None:
            print("Can't find player: " + name)
            return False
        else:
            self.players[ndx].remove_wanted()
            return True

    def add_wanted(self, name):
        ndx = self.get_index(name)
        if ndx is None:
            print("Can't find player: " + name)
            return False
        else:
            self.players[ndx].set_wanted()
            return True

    def save_csv(self, filename):
        # open file
        with open(filename, mode = 'w', newline='') as save_file:
            # create csv writer with proper delimiters
            writer = csv.writer(save_file, delimiter=',', quotechar='"')
            # put in header columns
            writer.writerow(['id', 'name', 'alive', 'death_time', 'killer', 'wanted',
            'wanted_time', 'kills'])

            # go thru alive players and add them to list
            for x in self.players:
                writer.writerow([x.id, x.name, x.alive, x.death_time, x.killer,
                x.wanted, x.wanted_time, ', '.join(x.kills)])

            # go thru dead players and add them to list
            for x in self.dead_players:
                writer.writerow([x.id, x.name, x.alive, x.death_time, x.killer,
                x.wanted, x.wanted_time, ', '.join(x.kills)])

    def load_csv(self, filename):
        with open(filename) as load_file:
            reader = csv.reader(load_file, delimiter=',')
            central = pytz.timezone('America/Chicago')
            line_count = 0
            for row in reader:
                # skip the first row of headers
                if line_count == 0:
                    line_count += 1
                else:
                    # reformatting strings
                    alive = True
                    want = True
                    dtime = -1
                    wtime = -1
                    if(row[2] == 'False'):
                        alive = False
                    if(row[2] == 'True'):
                        alive = True
                    if(row[5] == 'False'):
                        want = False
                    if(row[5] == 'True'):
                        want = True
                    if(row[3] != '-1'):
                        dtime = parse(row[3])
                    if(row[6] != '-1'):
                        wtime = parse(row[6])

                    # add player back into game
                    player = Player(row[1], int(row[0]), alive, dtime,
                    row[4], want, wtime, row[7].split())

                    # add them to proper list
                    if player.is_alive():
                        self.players.append(player)
                    else:
                        self.dead_players.append(player)
                    line_count += 1

    def log_event(self, filename, event, notes = ''):
        with open(filename, mode = 'a+') as log_file:
            log_file.write("Date: " + datetime.datetime.now(pytz.timezone('America/Chicago')).strftime("%Y-%m-%d %H:%M") + '\n')
            log_file.write("Event: " + event + '\n')
            log_file.write("Notes: " + notes + '\n\n')
