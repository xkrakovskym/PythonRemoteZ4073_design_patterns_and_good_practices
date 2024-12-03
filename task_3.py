"""
Zadání

	1.	Vytvořte třídu Enemy, která obsahuje následující vlastnosti:
	•	typ (např. “Ork”, “Troll”),
	•	zivoty (např. 100),
	•	utok (např. 20).
	2.	Implementujte metodu clone():
	•	Tato metoda vytvoří kopii instance Enemy.
	3.	Pomocí prototypu vytvořte základního nepřítele a klonujte ho, přičemž upravíte jeho vlastnosti (např. zvýšíte útok nebo snížíte životy).
"""


from copy import deepcopy

class Enemy:
    def __init__(self, typ, zivoty, utok):
        self.typ = typ
        self.zivoty = zivoty
        self.utok = utok
        self.specialni_vlastnosti = []

    def __str__(self):
        return f"Typ: {self.typ}, Životy: {self.zivoty}, Útok: {self.utok}, Speciální vlastnosti: {self.specialni_vlastnosti}"

    def clone(self):
        return(deepcopy(self))


# Hlavní program
if __name__ == "__main__":
    # TODO: Vytvořte základního nepřítele
    prototyp_enemy = Enemy("Troll", "100", "10")

    enemy_1 = prototyp_enemy.clone()
    enemy_1.specialni_vlastnosti.append("nesmrtelnost")

    enemy_2 = prototyp_enemy.clone()
    enemy_2.specialni_vlastnosti.append("odolnost voci magii")

    print(enemy_1)
    print(enemy_2)