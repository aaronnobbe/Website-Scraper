from dataclasses import dataclass
@dataclass
class Mineral:
    name: str
    color: str
    hardness: float

    def describe(self):
        return f"{self.name} is {self.color} and has a hardness of {self.hardness}"
    def hardness_calculate(self):
        if self.hardness < 5:
            return ", that's kinda squishy"
        elif self.hardness >=5 and self.hardness < 6:
            return ", that's hard"
        else:
            return ", that's rock hard"
       

if __name__ == "__main__":
    mineral1 = Mineral("Amethyst", "purple",5.33)
    mineral2 = Mineral("Quartz", "clear",6.21)
    print(mineral1.describe(), mineral1.hardness_calculate())
    print(mineral2.describe(), mineral2.hardness_calculate())