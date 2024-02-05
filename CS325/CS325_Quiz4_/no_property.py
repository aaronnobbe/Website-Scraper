class Rock:
    def __init__(self,rock_name,rock_category):

        self.name = rock_name
        self.category = rock_category

    def getname(self):
        return self._name
    
    
    def getcategory(self):
        return self._category
    
if __name__ == "__main__":
    rock1 = Rock("quartz", "mineral")
    print("This is a" , rock1.getname(), "and it's a" , rock1.getcategory())