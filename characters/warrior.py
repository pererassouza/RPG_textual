from .character import Character


class Warrior(Character):
    def __init__(self, name: str, raca: str) -> None:
        self.physical_damage = 15
        self.magical_damage = 0
        self.life = 70
        self.clss = "Warrior"
        super().__init__(name, raca, self.clss, self.physical_damage,
                         self.magical_damage, self.life)

    def basic_attck(self, en: Character):
        self.enemy = en
        self.enemy.life -= self.physical_damage
