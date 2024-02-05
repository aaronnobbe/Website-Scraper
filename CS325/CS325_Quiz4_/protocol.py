from typing import Protocol

class RockProtocol(Protocol):
    def formation(self):
        pass

    def looks(self):
        pass
    
class Amethyst:
    def formation(self):
        print("Amethysts are formed through the crystallization of quartz in volcanic rocks")

    def looks(self):
        print("Amethysts are purple and my favorite rock")

class Quartz:  
    def formation_(self):
        print("Quartz is formed in various ways one of which comes from magma")

    def looks(self):
        print("Quarts looks see through and crystalized")
if __name__ == "__main__":

    obj1 =Amethyst()
    obj1.formation()
    obj1.looks()

    obj2 =Quartz()
    obj2.formation()
    obj2.looks()