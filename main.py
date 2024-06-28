from characters import Mage
from characters import Warrior
from characters import Enemy
from characters import Orc
from world.battleCamp import BattleCamp
from world.history import Cenario

# Criar personagens
w1 = Warrior("Felipe", 'Human')
m1 = Mage("Ana", 'Human')
e1 = Enemy("Baldurs", "Goblin")
o1 = Orc("Orc", "Ogro")

# Criar cenário
c1 = Cenario()
c1.make_initial_history()

# Iniciar batalha
bc = BattleCamp(m1, o1)
bc.make_scene()
