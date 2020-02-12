class person:
    count=0 #class attribute
    def __init__(self): #constructor
        self.name="unknown" #instance attribute
        self.age=0 #instance attribute
    def displayInfo(self): #method
        print(self.name, self.age)
