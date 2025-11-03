import math
#1.Animals Speaks create a base class animal with method sound () . Subclasses :- Dog ->prints 'Bark' cat->prints 'Meow' 
#create a list of Animals and call sounnd for each
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")
animal_list = [Dog(),Cat()]
for animal in animal_list:
    animal.sound()

#2.calculator operatios create a base class calculator with method calculate (a,b) 
#sub classes:add->add two numbers ,subtract-> subtract two numbers .call calculate () for both
class calculator:
    def calculate(self,a,b):
        raise NotImplementedError("Subclass must implement this method")

class add(calculator):
    def calculate(self, a,b):
        return a+b
class subtract(calculator):
    def calculate(self, a,b):
        return a-b

plus=add()
minus=subtract()
print("Addition result:", plus.calculate(10,20))
print("Subtraction result:", minus.calculate(60, 10))

#3.3.Transport Ride fare class Transport with method fare(Distance) .Subclasses:-Bus->fare=distance*10-Train->fare=distance*5
#show polymorphismm by calling fare() with same distance
class Transport:
    def fare(self, distance):
        raise NotImplementedError("Subclass must implement this method")
class Bus(Transport):
    def fare(self, distance):
        return distance * 10
class Train(Transport):
    def fare(self, distance):
        return distance * 5

distance = 50  
transports = [Bus(), Train()]
for t in transports:
    print(f"{t.__class__.__name__} fare for {distance} km = {t.fare(distance)}")

#4.Shape Area Class Shape with method area(). Subclasses: - Square (side²) - Circle (π × r²) 
#Loop through objects and print areas.

class shape():
    def area():
        pass
class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)

shapes = [square(5), circle(3)] 
for s in shapes:
    print(f" Area of {s.__class__.__name__} = {s.area():.2f}")

#5.Employee Work Class Employee with method work().
#Subclasses: - Developer → prints 'Writing code' - Tester → prints 'Testing software' Call work() on both employees.

class Employee:
    def work(self):
        pass
class developer(Employee):
    def work(self):
        print("Writing code")
class tester(Employee):
    def work(self):
        print("Testing Software")

employees=[developer(),tester()]
for emp in employees:
    emp.work()

#Abstraction tasks
#6.Vehicle Start Abstract class Vehicle with method start().
#Subclasses: - Car → 'Car started' - Bike → 'Bike started'

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

# 7. Bank Account Abstract class BankAccount with method withdraw(amount).
#Subclasses:SavingsAccount → 'Withdrawn from savings' - CurrentAccount → 'Withdrawn from current'

from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"{amount} withdrawn from savings Account")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print(f"{amount} withdrawn from current Account")

savings = SavingsAccount()
current = CurrentAccount()

savings.withdraw(1000)   
current.withdraw(5000) 


#8.Device Power Abstract class Device with method power_on().
#Subclasses: - TV → 'TV is ON' Laptop → 'Laptop is ON'

from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

class TV(Device):
    def power_on(self):
        print("TV is ON")

class Laptop(Device):
    def power_on(self):
        print("Laptop is ON")

tv1 = TV()
laptop1 = Laptop()

tv1.power_on()       
laptop1.power_on()


#9.Student Exam Abstract class Exam with method start_exam().
#Subclasses: - MathExam → 'Mathexam started' - EnglishExam → 'English exam started'

from abc import ABC, abstractmethod
class Exam(ABC):
    @abstractmethod
    def start_exam(self):
        pass 

class MathExam(Exam):
    def start_exam(self):
        print("Math exam started")

class EnglishExam(Exam):
    def start_exam(self):
        print("English exam started")

math_exam = MathExam()
english_exam = EnglishExam()

math_exam.start_exam()      
english_exam.start_exam()   

#10.Report Generation Abstract class Report with method generate().
# Subclasses: - PDFReport → 'PDF Report generated' - ExcelReport → 'Excel Report generated'

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

pdf_report = PDFReport()
excel_report = ExcelReport()

pdf_report.generate()    
excel_report.generate() 




