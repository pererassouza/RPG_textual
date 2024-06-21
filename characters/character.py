from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self,
                 name: str,
                 race: str,
                 _clss: str,
                 _physical_damage: int,
                 _magical_damage: int,
                 _life: int):
        self.name = name
        self.race = race
        self.clss = _clss
        self.physical_damage = _physical_damage
        self.magical_damage = _magical_damage
        self.life = _life

    @abstractmethod
    def basic_attck(self, en): ...

    @property
    def show_character(self):
        print(f"Name: {self.name}\nClass: {self.clss}\nRace: {self.race}\n\
Physical damage: {self.physical_damage}\nMagical damage: {self.magical_damage}\
\nLife: {self.life}\n")
