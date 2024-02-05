class Rock:
    def __init__(self,rock_name,rock_category):

        self.name = rock_name
        self.category = rock_category
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
if __name__ == "__main__":
    rock = Rock("quartz", "mineral")
    print("This is a" , rock.name, "and it's a" , rock.category)