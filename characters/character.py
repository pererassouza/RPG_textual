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
        self.clss = _clss
        self.race = race
        self.physical_damage = _physical_damage
        self.magical_damage = _magical_damage
        self.life = _life

    @abstractmethod
    def show_character(self): ...

    @abstractmethod
    def basic_attck(self, en): ...
