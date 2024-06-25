from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self,
                 name: str,
                 race: str,
                 _life: int,
                 _clss: str | None = None,
                 _physical_damage: int = 1,
                 _magical_damage: int = 1,
                 _intimidar: int = 1,
                 _resistencia: int = 1):
        self.name = name
        self.race = race
        self.clss = _clss
        self.physical_damage = _physical_damage
        self.magical_damage = _magical_damage
        self.life = _life
        self._intimidar = _intimidar
        self.resistencia = _resistencia

    @abstractmethod
    def basic_attck(self, en): ...

    @abstractmethod
    def intimidar(self, en): ...

    @abstractmethod
    def power_up(self): ...
