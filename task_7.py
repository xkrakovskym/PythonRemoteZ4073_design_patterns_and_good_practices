"""
	1.	Ukládání uživatelů do souboru:
	•	Informace o uživateli budou obsahovat jméno, věk a seznam oblíbených položek (například filmy, knihy, hry).
	•	Informace o uživatelích se uloží do souboru pomocí Pickle.
	2.	Načítání uživatelů ze souboru:
	•	Aplikace umožní načíst data o uživatelích ze souboru a zobrazit je.
	3.	Přidávání a mazání uživatelů:
	•	Přidejte možnost přidat nového uživatele nebo smazat uživatele podle jeho jména.
	4.	Bezpečné ukončení programu:
	•	Při ukončení programu se veškeré změny v uživatelských datech uloží do souboru.


	Datová struktura:
	users = [
    {"jméno": "Alice", "věk": 25, "oblíbené": ["Pán prstenů", "Matrix"]},
    {"jméno": "Bob", "věk": 30, "oblíbené": ["Harry Potter", "Hvězdné války"]}
]
class User:
    def __init__(self, name, age, favorites):
        self.name = name
        self.age = age
        self.favorites = favorites

user1 = User("Michal", 29, ["Forest Gump"])

user1 = {"jméno": "Michal", "věk": 29, "oblíbené": ["Forest Gump"]}
"""


import pickle


# Funkce pro uložení uživatelů do souboru
def ulozit_uzivatele(users, soubor):
    """
    Uloží seznam uživatelů do souboru pomocí Pickle.
    """
    with open(soubor, "wb") as file:
        # TODO: Serializujte seznam `users` a uložte ho do souboru
        pass


# Funkce pro načtení uživatelů ze souboru
def nacist_uzivatele(soubor):
    """
    Načte seznam uživatelů ze souboru pomocí Pickle.
    Pokud soubor neexistuje, vrátí prázdný seznam.
    """
    try:
        with open(soubor, "rb") as file:
            # TODO: Načtěte seznam uživatelů ze souboru
            pass
    except FileNotFoundError:
        return []


# Funkce pro přidání uživatele
def pridat_uzivatele(users, jmeno, vek, oblibene):
    """
    Přidá nového uživatele do seznamu.
    """
    # TODO: Přidejte nového uživatele (slovník) do seznamu `users`
    pass


# Funkce pro smazání uživatele
def smazat_uzivatele(users, jmeno):
    """
    Smaže uživatele podle jeho jména.
    """
    # TODO: Smažte uživatele ze seznamu `users` podle `jmeno`
    pass


# Funkce pro zobrazení uživatelů
def zobrazit_uzivatele(users):
    """
    Vypíše seznam uživatelů na obrazovku.
    """
    # TODO: Vypište všechny uživatele (jméno, věk, oblíbené položky)
    pass


def main():
    soubor = "uzivatele.pkl"
    users = nacist_uzivatele(soubor)

    while True:
        print("\nMenu:")
        print("1. Zobrazit uživatele")
        print("2. Přidat uživatele")
        print("3. Smazat uživatele")
        print("4. Uložit a ukončit")

        volba = input("Vyberte akci: ")

        if volba == "1":
            zobrazit_uzivatele(users)
        elif volba == "2":
            jmeno = input("Jméno: ")
            vek = int(input("Věk: "))
            oblibene = input("Oblíbené položky (oddělené čárkou): ").split(", ")
            pridat_uzivatele(users, jmeno, vek, oblibene)
        elif volba == "3":
            jmeno = input("Jméno uživatele ke smazání: ")
            smazat_uzivatele(users, jmeno)
        elif volba == "4":
            ulozit_uzivatele(users, soubor)
            print("Data byla uložena. Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main()
