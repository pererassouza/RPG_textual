from characters import Mage
from characters import Warrior
from characters import Enemy
from world.battleCamp import BattleCamp
from world.history import Cenario

# Criar personagens
w1 = Warrior("Felipe", 'Human')
m1 = Mage("Ana", 'Human')
e1 = Enemy("Baldurs", "Goblin")

# Criar cenário
c1 = Cenario()
c1.make_initial_history()

# Iniciar batalha
bc = BattleCamp(m1, e1)
bc.make_scene()
