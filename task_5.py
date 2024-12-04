"""
	1.	Vytvořte dekorátor cache, který:
	•	Použije vnitřní slovník (dict) k ukládání výsledků na základě argumentů funkce.
	•	Zkontroluje, zda byly stejné argumenty již použity. Pokud ano, vrátí uložený výsledek.
	•	Pokud argumenty ještě nebyly použity, zavolá původní funkci, uloží výsledek a vrátí ho.
	2.	Dekorátor nepoužije functools.wraps.
	3.	Otestujte dekorátor na jednoduché funkci add(a, b), která sčítá dvě čísla.
	4.	Zkontrolujte, jak se změnily metadata funkce add (například __name__ a __doc__).
"""
import functools

# Krok 1: Implementace dekorátoru cache
def cache(fn):
    _cache = {}

    @functools.wraps(fn)
    def cacher(*args):
        if args in _cache:
            print("Cache hit")
            print(_cache)
            return _cache[args]
        else:
            result = fn(*args)
            _cache[args] = result
            print("Store cache")
            return result
    return cacher

@cache
def add(a, b):
    return a + b


# Krok 3: Použijte dekorátor cache na funkci add
#print(add.__name__)
# Krok 4: Zkontrolujte metadata funkce add

# Krok 5: Vytvořte novou funkci fibonaci a použijte dekorátor cache
@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)


print(fib(10))
print(fib(10))


# Kroky 6: Zkontrolujte ci ma kazda funkce svou vlastni cache

print(add(1,2))
print(add(1,2))
print(add(5,78))
print(add(5,78))