class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand,self.model} started")

    def stop_engine(self):
        print(f"{self.brand, self.model} stoped")

class Car(Vehicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.brand, self.model} isn honking: beep beep")


v1 = Vehicle("Toyota","Camry")
v1.start_engine()
v1.stop_engine()

c1 = Car("Honda","Hoda Civic","Petrol")
c1.start_engine()
c1.stop_engine()
c1.honk()
