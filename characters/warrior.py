from .character import Character


class Warrior(Character):
    def __init__(self, name: str, raca: str) -> None:
        self.physical_damage = 15
        self.magical_damage = 0
        self.life = 70
        self._intimidar = 2
        self.resistencia = 4
        self.clss = "Warrior"
        super().__init__(name, raca, self.life, self.clss,
                         self.physical_damage, self.magical_damage,
                         self._intimidar, self.resistencia)

    def basic_attck(self, en: Character):
        self.enemy = en
        dano_dado = self.physical_damage - en.resistencia
        self.enemy.life -= dano_dado

    def intimidar(self, en: Character):
        if en.clss == "Orc":
            en.resistencia -= self._intimidar - 1
        en.resistencia -= self._intimidar

    def power_up(self):
        self.magical_damage += 2
        self.physical_damage += 4
