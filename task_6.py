"""
	1.	Třída CustomerQueue:
	•	Reprezentuje frontu zákazníků.
	•	Obsahuje metody:
	•	add_customer(name): Přidá zákazníka do fronty.
	•	__iter__(): Vrátí instanci iterátoru.
	2.	Iterátor CustomerQueueIterator:
	•	Umožňuje přístup ke každému zákazníkovi ve frontě.
	•	Obsahuje metody:
	•	__iter__(): Vrátí iterátor (samotný objekt).
	•	__next__(): Vrátí dalšího zákazníka ve frontě. Pokud ve frontě nikdo není, vyvolá výjimku StopIteration.
	3.	Použití iterátoru:
	•	Použijte iterátor k iteraci přes zákazníky ve frontě a vypište jejich jména (jakoby byli obslouženi).
"""

class CustomerQueue:
    def __init__(self):
        self.customers = []

    def add_customer(self, name):
        self.customers.append(name)

    def __iter__(self):
        return CustomerQueueIterator(self.customers)


class CustomerQueueIterator:
    def __init__(self, customers):
        self.customers = customers
        self.index = 0  # Počáteční index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.customers):
            customer = self.customers[self.index]
            self.index += 1
            return customer
        else:
            raise StopIteration


# Úkol:
# 1. Vytvořte instanci třídy `CustomerQueue`.
# 2. Přidejte několik zákazníků do fronty.
# 3. Použijte iterátor k iteraci přes frontu zákazníků a vypište jejich jména.

# Příklad:
queue = CustomerQueue()
queue.add_customer("Jan")
queue.add_customer("Pavla")
queue.add_customer("Karel")

for customer in queue:
    print(f"Obsluhuji zákazníka: {customer}")


iterator = iter(queue)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    pass