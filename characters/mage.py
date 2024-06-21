from .character import Character


class Mage(Character):
    def __init__(self, name: str, race: str):
        self.physical_damage = 5
        self.magical_damage = 20
        self.life = 85
        self.clss = "Mage"
        super().__init__(name, race, self.clss,
                         self.physical_damage, self.magical_damage, self.life)

    def basic_attck(self, en: Character):
        en.life -= self.magical_damage
