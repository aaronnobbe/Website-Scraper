from typing import Protocol

class RockProtocol(Protocol):
    def formation_process(self):
        pass

    def characteristics(self):
        pass

class Amethyst:
    def formation_process(self):
        print("amethysts are formed from quartz in valcanoes.")

    def characteristics(self):
        print("Amethysts are purple.")

class Quartz:
    def formation_process(self):
        print("Quartz is also formed in valcanoes.")

    def characteristics(self):
        print("Quartz is pretty see through.")

if __name__ == "__main__":
    obj1 = Amethyst()
    obj1.formation_process()
    obj1.characteristics()

    obj2 = Quartz()
    obj2.formation_process()
    obj2.characteristics()
