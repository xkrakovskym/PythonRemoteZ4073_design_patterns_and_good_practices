def cache(fn):
    _cache = {}

    def cacher(*args):
        if args in _cache:
            print("Cache hit")
            return _cache[args]
        else:
            print("Store cache")
            result = fn(*args)
            _cache[args] = result
        return result

    return cacher

def add(a, b):
    return a + b

add = cache(add)
print(add(1,2))
print(add(1,2))