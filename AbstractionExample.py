from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,no_of_tyres):
        self.no_of_tyres = no_of_tyres

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print(" vehicle stops")

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
    def start(self):
        print("Car starts")


class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)

    def start(self):
        print("Bike starts")

    def speed(self):
        print("bike speeds")


class Truck(Vehicle):
    def __init__(self):
        super().__init__(4)





#v1 = Vehicle(4)
c1 = Car()
c1.start()
c1.stop()

b1 = Bike()
b1.start()
b1.stop()
b1.speed()


v1 = Vehicle(4)
v1.start()
v1.stop()

t1 = Truck()
t1.start()
t1.stop()