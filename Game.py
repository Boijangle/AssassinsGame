class Game:
    def __init__(self):
        self.players = []

    def add_players(self, player):
        self.players.append(player)

    def print_players(self):
        for x in self.players:
            x.print_player()
            print("\n")
