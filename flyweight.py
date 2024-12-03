import random

class Engine:
    instances = 0

    def __init__(self, identifier, volume, engine_type):
        Engine.instances += 1
        self._identifier = identifier
        self._volume = volume
        self._engine_type = engine_type


class Car:
    def __init__(self, producer, vin, model_name, engine):
        self._producer = producer
        self._vin = vin
        self._model_name = model_name
        self._engine = engine


class CarFactory:       # drzime iba 4 objekty na ako class variable
    engines = [Engine('polo', 1.6, 'DIESEL'),
               Engine('poloGTI', 2.0, 'GASOLINE'),
               Engine('golf', 1.5, 'GASOLINE')]

    @staticmethod
    def create_vw_polo(vin):
        return Car('VW', vin, 'Polo', CarFactory.engines[0])

    @staticmethod
    def create_vw_polo_gti(vin):
        return Car('VW', vin, 'Polo GTI', CarFactory.engines[1])

    @staticmethod
    def create_vw_golf(vin):
        return Car('VW', vin, 'Golf', CarFactory.engines[2])


def generate_vin():
    return random.randint(1000000, 99999999)


def main():
    produced_cars = []
    car_creation_methods = {
        0: CarFactory.create_vw_polo,
        1: CarFactory.create_vw_polo_gti,
        2: CarFactory.create_vw_golf,
    }

    for _ in range(10000):
        engine_type = random.randint(0, 2)
        vin = generate_vin()
        car_creation_method = car_creation_methods[engine_type]
        produced_cars.append(car_creation_method(vin))

    print(f"I created {len(produced_cars)} cars, but only {Engine.instances} references to Engine objects")


if __name__ == '__main__':
    main()
