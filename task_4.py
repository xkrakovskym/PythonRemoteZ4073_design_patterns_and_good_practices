"""
Popis Úkolu

	1.	Vytvořte rodičovskou třídu Employee (již připravená) pro reprezentaci zaměstnance se jménem a platem.
	2.	Rozšiřte tuto třídu pomocí třídy Manager, která přidá atribut department (oddělení).
	3.	Použijte super() v konstruktoru (__init__) třídy Manager, abyste inicializovali atributy rodičovské třídy.
	4.	Přepište metodu details() v třídě Manager, abyste využili rodičovskou implementaci pomocí super().details() a přidali informace o oddělení.



"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        # TODO: Zavolejte __init__ rodičovské třídy pomocí
        pass

    def details(self):
        # TODO: Zavolejte metodu details rodičovské třídy pomocí
        pass


# Úkol:
# 1. Vytvořte instanci třídy Manager.
# 2. Použijte metodu details(), aby zobrazila všechny informace.