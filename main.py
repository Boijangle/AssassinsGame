from Player import Player
from Game import Game

g = Game()
p = Player("Dylan")
t = Player("Casey")
y = Player("Billy")
j = Player("Joe")

g.add_players(p)
g.add_players(t)
g.add_players(y)
g.add_players(j)

print("INITIAL")
g.print_players()

g.attempt_kill("Dylan", "Joe")


print("ALIVE")
g.print_players()
print("DEAD")
g.print_dead_players()
