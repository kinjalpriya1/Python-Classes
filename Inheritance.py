#parent 
class A: 
    def __init__(self):
        self.x = 10
        self.y = 20
    def f1(self):
        print("f1 from class A")

#child
class B(A):
    pass

a = A()
print(a.x)
print(a.y)
a.f1()
print(a.__dict__)
b = B()
print(b.__dict__)
b.f1()


#Assignment 1

class Vehicle:
    def move(self):
        print("The vehicle is moving")


class Car(Vehicle):
    def honk(self):
        print("Car goes honk!")

class Bike(Vehicle):
    def kickStart(self):
        print("Bike kick-started!")

c = Car()
c.move()
c.honk()

b = Bike()
b.move()
b.kickStart()



#LESSON:

#parent class/ super class/ base class/ derived class
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("A class object is created")
    def f1(self):
        print("f1 from A")

#child class/deriving class
class B(A):
    def __init__(self,x,y,z):
        #associated parent class object
        super().__init__(x,y)
        self.z = z
        print("B class object is created")

        def f2(self):
            print("f2 from B")

# whenever you create any object, internally constructor(__init__) method
# a = A(10,20)
# b = B(30)
# a = A(10,20)
b = B(1,2,100)
#b.f2()
b.f1()


#ASSIGNMENT 2: Employee Payroll System

class Employee():
    def __init__(self, name, id, basicSalary, hra, da, tax):
        self.name = name
        self.id = id
        self.basicSalary = basicSalary
        self.hra = hra
        self.da = da
        self.tax = tax
        print("Employee class object is created")

    def grossSalary(self):
        hraAmount = self.hra / 100
        daAmount = self.da / 100
        totalSal = self.basicSalary + hraAmount + daAmount
        return totalSal

    def netSalary(self):
        grossAmount = self.grossSalary()
        final = grossAmount - (grossAmount * self.tax)
        #print(f"Salary: {self.final}")
        return final

    def details(self):
        print(f"""
Name: {self.name}
ID: {self.id}
Base Salary: {self.basicSalary}
HRA: {self.hra}
DA: {self.da}
Gross Salary: {self.grossSalary()}
Salary: {self.netSalary()}
        """)

#e = Employee("Bob", "7913245", 50000, 20, 13, 0.13)
#e.grossSalary()
#e.netSalary()
#e.details()

class Manager(Employee):
    def __init__(self, name, id, basicSalary, hra, da, tax, department, managementAllowance):
        self.name = name
        self.id = id
        self.basicSalary = basicSalary
        self.hra = hra
        self.da = da
        self.tax = tax
        self.department = department
        self.allowance = managementAllowance
 

    # def details(self):
    #     print(f"""
    #     Department: {self.department}
    #     Management Allownace: {self.allowance}
    #     """)

class Developer(Employee):
    def __init__(self, name, id, basicSalary, hra, da, tax, progLanguage, projectAllowance):
        self.name = name
        self.id = id
        self.basicSalary = basicSalary
        self.hra = hra
        self.da = da
        self.tax = tax
        self.language = progLanguage
        self.allowance = projectAllowance

    def grossSalary(self):
            self.grossSalary(self) 
            totalSal += self.allowance 

    # def details(self): 
    #     print(f"""
    #     Programming Language: {self.departement}
    #     Project Allownace: {self.allowance}
    #     """)

priya = Manager("Priya", "M101", 50000, 20, 10, 0.10, "Sales", 10000)
rahul = Manager("Rahul", "D101", 40000, 20, 10, 0.10, "Python", 5000)
priya.details()
    

    