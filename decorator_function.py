import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the func")

        result = func(*args, **kwargs)

        print("After calling the func")

        return result
    return wrapper

@my_decorator
def say_hello(name):
    """
    says hello to a person with a given name
    """
    print(f"Hello {name}!")


say_hello("Michal")
print(say_hello.__name__)