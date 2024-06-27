from .character import Character


class Mage(Character):
    def __init__(self, name: str, raca: str):
        self.physical_damage = 5
        self.magical_damage = 20
        self.life = 60
        self._intimidar = 2
        self.resistencia = 5
        self.clss = "Mage"
        super().__init__(name, raca, self.life, self.clss,
                         self.physical_damage, self.magical_damage,
                         self._intimidar, self.resistencia)

    def basic_attck(self, en: Character):
        en.life -= self.magical_damage - en.resistencia

    def intimidar(self, en: Character):
        if en.clss == "Warrior":
            en.resistencia -= self._intimidar - 1
        en.resistencia -= self._intimidar

    def power_up(self, *args):
        self.magical_damage += 5
        self.physical_damage += 2
