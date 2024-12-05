"""
	1.	Vytvořte rozhraní Observer (sledovatel):
	•	Deklarujte metodu update(player), která přijme aktuální stav hráče a provede odpovídající akci.
	2.	Vytvořte třídu Player (hráč):
	•	Obsahuje atributy health a energy.
	•	Má metody pro změnu health a energy.
	•	Implementuje správu sledovatelů (add_observer, remove_observer) a notifikaci sledovatelů (notify_observers).
	3.	Vytvořte sledovatele (Observers):
	•	Healer: Sleduje zdraví hráče a pokud klesne pod 50, automaticky zvýší zdraví o 10 bodů.
	•	Energy Manager: Sleduje energii hráče a pokud klesne pod 30, zobrazí varování.
	4.	Simulujte změny:
	•	Změňte stav hráče (zdraví, energii) a sledujte, jak sledovatelé reagují.
"""

from abc import ABC, abstractmethod


# Rozhraní Observer
class Observer(ABC):
    @abstractmethod
    def update(self, player):
        pass


# Třída Player (hráč)
class Player:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self.observers = []  # Seznam sledovatelů

    def add_observer(self, observer):
        """Přidá sledovatele."""
        # TODO: Přidejte sledovatele do seznamu
        pass

    def remove_observer(self, observer):
        """Odebere sledovatele."""
        # TODO: Odeberte sledovatele ze seznamu
        pass

    def notify_observers(self):
        """Notifikuje všechny sledovatele."""
        # TODO: Informujte všechny sledovatele o změně stavu
        pass

    def change_health(self, value):
        """Změní zdraví a notifikuje sledovatele."""
        self.health += value
        self.notify_observers()

    def change_energy(self, value):
        """Změní energii a notifikuje sledovatele."""
        self.energy += value
        self.notify_observers()


# Sledovatel Healer
class Healer(Observer):
    def update(self, player):
        """Pokud zdraví hráče klesne pod 50, zvýší zdraví."""
        # TODO: Implementujte logiku pro zvýšení zdraví hráče
        pass


# Sledovatel Energy Manager
class EnergyManager(Observer):
    def update(self, player):
        """Pokud energie hráče klesne pod 30, zobrazí varování."""
        # TODO: Implementujte logiku pro varování o nízké energii
        pass


# Hlavní program
def main():
    # Vytvoření hráče
    player = Player(health=100, energy=100)

    # Vytvoření sledovatelů
    healer = Healer()
    energy_manager = EnergyManager()

    # Přidání sledovatelů k hráči
    player.add_observer(healer)
    player.add_observer(energy_manager)

    # Simulace změn ve stavu hráče
    print("\nZměna zdraví hráče o -60:")
    player.change_health(-60)  # Zdraví klesne na 40

    print("\nZměna energie hráče o -80:")
    player.change_energy(-80)  # Energie klesne na 20


if __name__ == "__main__":
    main()
