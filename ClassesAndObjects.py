'''
# Functional programming
greet = "Good morning"
def printHello():
    print("Hello",greet)
    for i in range(5):
        print(i)

printHello()


# OOP programming
class GREETING:
    greet = "Good morning"
    def printHello(self):
        print("Hello",self.greet)
    def printBye(self):
        print("Bye")

obj1 = GREETING()
print(obj1.greet)
obj1.printHello()
obj1.printBye()

obj2 = GREETING()
print(obj2.greet)
obj2.printHello()
obj2.printBye()




# Constructor ( default constecutor usage )

class Student:
    name = "Akshay"
    rollnum = 20
    def printStudentDetail(self):
        print("Name of Studnet is ",self.name," and roll number is ",self.rollnum)

std1 = Student()
std1.printStudentDetail()

'''

# create students with diffrenet names and rollnumber
# in this case we need to use parameterized constrcutor

class Student:
    def __init__(self,name,rollnum):
        self.name = name
        self.rollnum = rollnum

    def printStudentDetail(self):
        print("Name of Studnet is ",self.name," and roll number is ",self.rollnum)

std1 = Student("Rajesh",10)
std1.printStudentDetail()

std2 = Student("Mohan",12)
std2.printStudentDetail()
