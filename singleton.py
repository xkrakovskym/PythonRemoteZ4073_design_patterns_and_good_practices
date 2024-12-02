class ConfigSingleton:
    _instance = None

    def __init__(self):
        self.value = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            # Initialize any attributes of the singleton here, if necessary
            cls._instance.value = "Default Configuration"
        return cls._instance



config1 = ConfigSingleton()
config2 = ConfigSingleton()
print(config1==config2)