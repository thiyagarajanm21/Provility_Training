#Methods in python
#Instance Method
print("Instance Method")
class Company:
    def __init__(self,emp_name,emp_salary):
        self.emp_name=emp_name
        self.emp_salary=emp_salary
    def display(self):
        print(f"Employee name : {self.emp_name}\nEmployee Salary : {self.emp_salary}")
com = Company("Kumar",35000)
com.display()

#Static Method
print("Static Methods")
class Car:
    @staticmethod
    def drive(name):
        return f"{name} drive the car"
print(Car.drive("John"))

#Class Method
print("Class Method")
class Bank:
    ac_holder="Smith"
    @classmethod
    def updated(cls,name):
        cls.ac_holder=name
print(Bank.ac_holder)
Bank.updated("Michel")
print(Bank.ac_holder)

