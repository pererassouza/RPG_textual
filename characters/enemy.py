from .character import Character


class Enemy(Character):
    def __init__(self, name: str, raca: str):
        self.clss = 'Enemy'
        self.physical_damage = 5
        self.magical_damage = 15
        self.life = 40
        self._intimidar = 1
        self.resistencia = 5
        super().__init__(name, raca, self.life, self.clss,
                         self.physical_damage, self.magical_damage,
                         self._intimidar, self.resistencia)

    def basic_attck(self, en: Character):
        en.life -= self.magical_damage - en.resistencia

    def power_up(self, *args):
        self.magical_damage += 1
        self.physical_damage += 1

    def intimidar(self, en: Character):
        en.resistencia -= self._intimidar
