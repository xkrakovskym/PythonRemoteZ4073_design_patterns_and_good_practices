import time
from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, traffic_light):
        pass


class GreenLightState(TrafficLightState):
    def handle(self, traffic_light):
        print("Green -> Orange")
        traffic_light.state = OrangeLightState()


class OrangeLightState(TrafficLightState):
    def handle(self, traffic_light):
        print("Orange -> Red")
        traffic_light.state = RedLightState()


class RedLightState(TrafficLightState):
    def handle(self, traffic_light):
        print("Red -> Green")
        traffic_light.state = GreenLightState()


class TrafficLight:
    def __init__(self):
        self.state = GreenLightState()

    def change(self):
        self.state.handle(self)


traffic_light = TrafficLight()


for _ in range(10):
    traffic_light.change()
    time.sleep(1)
