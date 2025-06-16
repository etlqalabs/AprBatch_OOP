#1.  Method overloading ( not allowed in python )
'''
class MathsOperation:
    def addtion(self,a,b):
        print(a+b)

    def addtion(self, a, b,c):
        print(a+b+c)

ma = MathsOperation()
ma.addtion(2,3,5)
'''

# 2 . method overriding

class AdditionInBaseClass:
    def addtion(self,a,b):
        print("addiiton in base class",a+b)

class AdditionInChildClass(AdditionInBaseClass):
    def addtion(self,a,b):
        print("addiiton in child class",a+b)

addChild =  AdditionInChildClass()
addChild.addtion(2,4)

addChild =  AdditionInBaseClass()
addChild.addtion(2,4)


