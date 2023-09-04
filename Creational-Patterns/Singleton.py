class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


sing1 = Singleton()
sing2 = Singleton()
sing1.set_value(10)
print(sing2.get_value())

