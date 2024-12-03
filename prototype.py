from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Enemy(Prototype):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Enemy(name={self.name}, health={self.health}, attack_power={self.attack_power})"


base_enemy = Enemy(name="Troll", health=100, attack_power=50)

enemy1 = base_enemy.clone()
enemy1.name = "Troll Hunter"

enemy2 = base_enemy.clone()
enemy2.attack_power = 70
