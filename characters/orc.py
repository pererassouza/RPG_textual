from .character import Character


class Orc(Character):
    def __init__(self, name: str, raca: str) -> None:
        self.physical_damage = 15
        self.magical_damage = 0
        self.life = 70
        self._intimidar = 2
        self.resistencia = 4
        self.clss = "Enemy"
        super().__init__(name, raca, self.life, self.clss,
                         self.physical_damage, self.magical_damage,
                         self._intimidar, self.resistencia)

    def basic_attck(self, en: Character):
        self.enemy = en
        self.enemy.life -= self.physical_damage - en.resistencia

    def intimidar(self, en: Character):
        if en.clss == "Mage":
            en.resistencia -= self._intimidar - 1
        self.enemy.resistencia -= self._intimidar

    def power_up(self, *args):
        self.magical_damage += 1
        self.physical_damage += 2
