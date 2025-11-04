#Duck Typing Tasks
#1.Walk Like a Duck
"""Create two classes Duck and Person.
Both should have a method walk().
Write a function make_it_walk(obj) that accepts any object and calls walk().
Pass objects of both classes and observe
"""
class Duck:
    def walk(self):
        print("Duck is walking gracefully towards the pond.")

class Person:
    def walk(self):
        print("Person is walking to the office.")

def make_it_walk(obj):
    obj.walk()

duck1 = Duck()
person1 = Person()

make_it_walk(duck1)
make_it_walk(person1)

#2.Media Player Example
"""Create two classes:
MP3 → with method play()
Video → with method play()
Write a function start_media(obj) to call play() no matter the type.
"""
class MP3:
    def play(self):
        print("Playing MP3 audio... 🎵")

class Video:
    def play(self):
        print("Playing video file... 🎬")

def start_media(obj):
    obj.play()

song = MP3()
movie = Video()

start_media(song)   
start_media(movie)

#3. Payment System
"""Create two classes:
CreditCard → with method pay(amount)
UPI → with method pay(amount)
Write a function process_payment(obj, amount) to call pay()
"""
class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

def process_payment(obj, amount):
    obj.pay(amount)

card_payment = CreditCard()
upi_payment = UPI()

process_payment(card_payment, 5000)
process_payment(upi_payment, 1200)

#Abstraction Tasks
#4.Shape Area (Abstract)
"""Create an abstract class Shape with an abstract method area().
Subclasses:
Square → calculates side²
Circle → calculates πr²      """

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

square1 = Square(5)
circle1 = Circle(3)

print(f"Area of Square:{square1.area()} sq.units")
print(f"Area of Circle:{circle1.area():.2f} sq.units")

#5.Vehicle Start (Abstract)
"""Create an abstract class Vehicle with an abstract method start().
Subclasses:
Car → prints "Car started"
Bike → prints "Bike started"        """

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()

#6.Bank Account (Abstract)
"""Create an abstract class BankAccount with abstract method withdraw(amount).
Subclasses:
SavingsAccount → withdraw allowed if balance > 500
CurrentAccount → no minimum balance check
"""
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass 

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self.balance -= amount
            print(f"Withdrawn {amount}/-Rs from Savings Account. Remaining balance:Rs.{self.balance}")
        else:
            print("Cannot withdraw!Minimum balance of Rs.500 must be maintained.")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}/-Rs from Current Account. Remaining balance:Rs.{self.balance}")
        else:
            print("Insufficient balance!")

savings = SavingsAccount(2000)
current = CurrentAccount(3000)

savings.withdraw(1200)   
savings.withdraw(800)    

current.withdraw(2500)   
current.withdraw(1000)   

#7.Report Generation (Abstract)
"""Create an abstract class Report with abstract method generate().
Subclasses:
PDFReport → prints "PDF Report generated"
ExcelReport → prints "Excel Report generated"    """

from abc import ABC, abstractmethod
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF Report generated")

class ExcelReport(Report):
    def generate(self):
        print("Excel Report generated")

pdf = PDFReport()
excel = ExcelReport()

pdf.generate()
excel.generate()

#8.. Employee Work (Abstract)
"""Create an abstract class Employee with an abstract method work().
Subclasses:
Developer → prints "Writing code"
Tester → prints "Testing software"     """

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass 

class Developer(Employee):
    def work(self):
        print("Writing code")

class Tester(Employee):
    def work(self):
        print("Testing software")

dev = Developer()
test = Tester()

dev.work()
test.work()

#9.Appliance Power (Abstract)
"""Create an abstract class Appliance with abstract method turn_on().
Subclasses:
Fan → prints "Fan is ON"
Light → prints "Light is ON"   """

from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass 

class Fan(Appliance):
    def turn_on(self):
        print("Fan is ON")

class Light(Appliance):
    def turn_on(self):
        print("Light is ON")

fan = Fan()
light = Light()

fan.turn_on()
light.turn_on()





