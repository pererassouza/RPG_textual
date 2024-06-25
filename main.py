from characters import Mage
from characters import Warrior
from characters import Enemy
from world.battleCamp import BattleCamp
from world.history import Cenario


w1 = Warrior("Felipe", 'Human')
m1 = Mage("Ana", 'Human')
e1 = Enemy("Baldurs", "Goblin")
c1 = Cenario()

bc = BattleCamp(m1, e1)
bc.make_scene()
