class example:
    def __init__(self,name):
        self.name = name

    def __init__(self, name,rollnum):
        self.name = name
        self.rollnum = rollnum

    def Printdetails(self):
        print(self.name ,self.rollnum)


obj1 = example("ETL",10)
obj1.Printdetails()
