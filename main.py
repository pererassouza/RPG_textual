from characters import Mage
from characters import Warrior
from characters import Enemy
from world.battleCamp import BattleCamp
from world.history import Cenario


w1 = Warrior("Felipe", 'Human')
m1 = Mage("Ana", 'Human')
e1 = Enemy("Baldurs", "Goblin")

# w1.show_character
# m1.show_character
# e1.show_character

bc = BattleCamp(m1, e1)
c1 = Cenario()

c1.make_initial_history()
bc.make_scene()
