class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def displaydetails(self):
        print(f"CAR BRAND :{self.brand} \nMODEL :{self.model}")
car1 = Car("Toyota","Camry")
car1.displaydetails()

#INHERITANCE
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def displayinfo(self):
        print(f"Car Brand :{self.brand}\nCar Model :{self.model}")
c = Car("Hyudai","Creta")
c.displayinfo()