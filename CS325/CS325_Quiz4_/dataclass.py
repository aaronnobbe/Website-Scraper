from dataclasses import dataclass

@dataclass
class Mineral:
    name: str
    color: str
    hardness: float

    def desrcribe(self):
        return f"{self.name} is {self.color} and has a hardness of {self.hardness}"
if __name__ == "__main__":
    mineral1 = Mineral("Amethyst", "purple",5.33)
    mineral2 = Mineral("Quartz", "clear",6.21)
    print(mineral1.describe(),mineral2.describe())
