"""
Představte si scénář objednávkového systému pizzerie, kde si zákazníci mohou přizpůsobit pizzu výběrem různých příloh,
typů kůrky a velikostí. Použijte vzor Builder a zapouzdřete konstrukci pizzy způsobem,
který udržuje proces konstrukce oddělený od reprezentace, aby bylo snadné přidávat nové možnosti bez úpravy stávajícího kódu.
"""


class Pizza:
    def __init__(self):
        self.topping: list
        self.dough = None
        self.size = None

    def __str__(self):
        return f"Pizza with {self.topping}, {self.dough} dough and size {self.size}."


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def build(self):
        return self._pizza


### Vyrobit 3 pizzy s různými příchutěmi, kůrkami a velikostmi