#Class AND Object

print("--------CLASS AND OBJECT---------")
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def displaydetails(self):
        print(f"CAR BRAND :{self.brand} \nMODEL :{self.model}")
car1 = Car("Toyota","Camry")
car1.displaydetails()

#INHERITANCE
print("--------INHERITANCE---------")
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

#Polymorphism
print("--------POLYMORPHISM---------")
class Animal:
    def makesound(self):
        pass
class Dog(Animal):
    def makesound(self):
        return "bark"
class Cat(Animal):
    def makesound(self):
        return "meow"

a = [Dog(),Cat()]
for animals in a:
    print(animals.makesound())

#Encapsulation
print("--------ENCAPSULATION-------")
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def displaybalance(self):
        return self.__balance
bank = BankAccount(1000)
bank.deposit(500)
print(bank.displaybalance())

#Abstraction
print("------ABSTRACTION-----")
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())




