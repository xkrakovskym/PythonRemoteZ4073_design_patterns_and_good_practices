from abc import ABC, abstractmethod


class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding sugar and lemon")


class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")


tea = Tea()
coffee = Coffee()

print("making tea....")
tea.prepare_recipe()

print("making coffee....")
coffee.prepare_recipe()
