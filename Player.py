class Player:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.wanted = False
        self.wanted_time = -1

    def print_player(self):
        print(self.name, self.is_alive, self.wanted, self.wanted_time, sep="\n")
