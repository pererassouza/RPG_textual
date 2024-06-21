from characters import Mage
from characters import Warrior
from characters import Enemy
from world.battleCamp import BattleCamp


w1 = Warrior("Felipe", 'Human')
m1 = Mage("Ana", 'Human')
e1 = Enemy("Baldurs", "Goblin")

w1.show_character
m1.show_character
e1.show_character

bc = BattleCamp(m1, e1)
bc.make_scene()
