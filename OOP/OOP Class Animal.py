# class Animal:
#     def __init__(self,name, age, colour):
#         self.name = name
#         self.age = age
#         self.colour = colour
#         print("xyz")
#     def walk(self):
#         print(f"{self.name} is walking")
#     def displayInfo(self):
#         print(f"""
# Name: {self.name}
# Age: {self.age}
# Colour: {self.colour}
#         """)

# elephant = Animal("Elephant", 15, "Grey")
# lion = Animal("Lion", 10, "Orange")
# dog = Animal("Dog", 7, "Brown")
# elephant.walk()
# lion.walk()
# print(lion.name)
# lion.name = "Lion Sharma"
# print(lion.name)
# dog.displayInfo()
# lion.displayInfo()

# class Student:
#     def __init__(self, name, rollNumber, mathMarks, bioMarks, csMarks, englishMarks):
#         self.name = name
#         self.rollNum = rollNumber
#         self.math = mathMarks
#         self.bio = bioMarks
#         self.cs = csMarks
#         self.eng = englishMarks

#     def getGrade(self):
#         marks = (self.math + self.bio + self.cs + self.eng) / 4
#         if marks >= 90:
#             print("Grade A")
#         elif marks >= 75:
#             print("Grade B")
#         elif marks >= 60:
#             print("Grade C")
#         else:
#             print("Grade D")

#     def displayInfo(self):
#          print(f"""
# Name: {self.name}
# Roll #: {self.rollNum}
# Math: {self.math}
# Bio: {self.bio}
# CS: {self.cs}
# English: {self.eng}
#         """)

# Katherine = Student("Katherine", 1, 93, 87, 97, 81)
# Stefan = Student("Stefan", 2, 98, 84, 96, 93)
# Damon = Student("Damon", 3, 73, 68, 87, 70)
# Katherine.displayInfo()
# Katherine.getGrade()
# Stefan.displayInfo()
# Stefan.getGrade()
# Damon.displayInfo()
# Damon.getGrade()

class BankAccount:
    def __init__(self, number, name, __Balance__):
        self.number = number
        self.name = name
        self.__Balance__ = __Balance__

    def deposit(self):
        print(f"You have ${self.__Balance__} in your account")
        amount = int(input("How much do you want to add: "))
        self.__Balance__ += amount
        print(f"You have ${self.__Balance__} in your account")

    def withdraw(self):
        print(f"You have ${self.__Balance__} in your account")
        amount = int(input("How much do you want to withdraw: "))
        if amount <= self.__Balance__: 
            self.__Balance__ -= amount
            print(f"You have ${self.__Balance__} in your account")
        else:
            print("Not enough money.")

    def send(self, otherAccount):
        receiver = input("Who do you want to send money to: ")
        receiverID = int(input("What is their bank number: "))
        amount = int(input("How much do you want to send: "))
        if amount <= self.__Balance__: 
            self.__Balance__ -= amount
            otherAccount.__Balance__ += amount
            print(f"You have transfered {amount} to {otherAccount.name}")
            print(f"You have ${self.__Balance__} in your account") 
        else:
            print("Not enough money.")

    def receive(self,amount):
        self.__Balance__ += amount



    def displayInfo(self):
        print(f"""
# Name: {self.name}
# Bank ID: {self.number}
# __Balance__: {self.__Balance__}
#         """)

Bella = BankAccount(19185, "Bella Lewis", 1400000)
Elena = BankAccount(18640, "Elena Gilbert", 1270000)
Bella.displayInfo()
Bella.deposit()
Bella.withdraw()
Bella.send(Elena)
Elena.displayInfo()
