from .character import Character


class Enemy(Character):
    def __init__(self, name: str, race: str):
        self.clss = 'Enemy'
        self.physical_damage = 5
        self.magical_damage = 3
        self.life = 40
        super().__init__(name, race, self.clss,
                         self.physical_damage,
                         self.magical_damage, self.life)

    def basic_attck(self, en: Character):
        en.life -= self.magical_damage
