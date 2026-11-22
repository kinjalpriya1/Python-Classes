#The 4 main things in OOP:
# Encapsculation: private, 
# Inheritance
# Recurssion 
# Polymorphism (overriding)
# Abstraction

#In 2002
from abc import ABC, abstractmethod

class Tesla(ABC):
    @abstractmethod
    def autoDrive(self):
        pass
    @abstractmethod
    def runOnBattery(self):
        pass
    def drive(self):
        print("Car is being driven")

#In 2013
#t = Tesla()  can't create an object for an abstract class 
class Model1(Tesla):
    def autoDrive(self):
        print("Tesla is on autopilot mode")
    def runOnBattery(self):
        print("Tesla is running on battery")

m = Model1()


#Exalidraw
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    def resize(self):
        pass
    @abstractmethod
    def changeBackground(self):
        pass
    @abstractmethod
    def duplicate(self):
        pass
        #@abstractmethod



#Payment

#Bank - Payment
# Mode
# credit card
# upi payment 
# debitcard
#from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def payOnline(self):
        pass
    @abstractmethod
    def payOffline(self):
        pass

# p = Payment()
class CreditCard(Payment):
    def payOnline(self):
        print("online payment by credicard")
    def payOffline(self):
        print("online payment by debitcard")

class UPI(Payment):
    def payOnline(self):
        print("online payment by upi")
    def payOffline(self):
        print("online payment by upi")

class DebitCard(Payment):
    def payOnline(self):
        print("online payment by debicard")
    def payOffline(self):
        print("online payment by debitcard")

