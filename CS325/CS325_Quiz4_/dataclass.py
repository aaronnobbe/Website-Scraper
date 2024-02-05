from dataclasses import dataclass

@dataclass
class Mineral:
    name: str
    color: str
    hardness: float = 0.0

    def describe(self):
        return f"{self.name} is {self.color} and has a hardness of {self.hardness}"

if __name__ == "__main__":
    mineral = Mineral("Quartz", "Colorless", 7.0)
    print(mineral.describe())
