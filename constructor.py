# Doubt Session

class example:


    def __init__(self, name,rollnum):
        self.name = name
        self.rollnum = rollnum

    def __init__(self,name):
        self.name = name

    def Printdetails(self):
        print(self.name ,self.rollnum)


# doesn't work , it will always consider the last constructor
obj1 = example("ETL")
obj1.Printdetails()

obj2 = example("ETL",10)
obj2.Printdetails()
