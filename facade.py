class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")


class Thermostat:
    def set_temperature(self, temperature):
        print(f"Setting temperature to {temperature} degrees")


class SecuritySystem:
    def arm(self):
        print("The security system is armed")

    def disarm(self):
        print("The security system is disarmed")


class HomeAutomationFacade:
    def __init__(self, light, thermostat, security_system):
        self.light = light
        self.thermostat = thermostat
        self.security_system = security_system

    def leave_home(self):
        print("leaving home")
        self.light.off()
        self.thermostat.set_temperature(18)
        self.security_system.arm()

    def arrive_home(self):
        print("Arriving home")
        self.light.on()
        self.thermostat.set_temperature(22)
        self.security_system.disarm()


home_automation = HomeAutomationFacade(Light(), Thermostat(), SecuritySystem())

home_automation.leave_home()