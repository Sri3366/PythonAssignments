#single Inheritance
"""1.Bank Account System - Create a BankAccount class with attributes: account_number, balance. 
Add methods: deposit(), withdraw(). - Create a child class SavingsAccount that adds an attribute
interest_rate and a method add_interest()."""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance = {self.balance}")
        else:
            print("Insufficient balance")

class SavingsAccount(BankAccount):  # Child class
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)  # call parent constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New balance = {self.balance}")

savings_acc = SavingsAccount(12345, 1000, 5) 

savings_acc.deposit(500)      
savings_acc.withdraw(200)
savings_acc.add_interest()

"""2.Library Management - Parent class: Book with attributes title, author. - Child class: EBook with an
 extra attribute file_size and a method download()
"""
class Book: #parent class
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book: {self.title}, Author: {self.author}")

class EBook(Book): # Child class
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # call parent constructor
        self.file_size = file_size  # additional attribute

    def download(self):
        print(f"Downloading {self.title} ({self.file_size}MB)...")

ebook1 = EBook("Python Programming", "Sri Venkat", 50)

ebook1.display_info()  # inherited method from Book
ebook1.download()      # method of EBook

"""3.Employee Management - Parent class: Employee with attributes name, salary. - Child class:
Developer with an extra attribute programming_language.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)  # call parent constructor
        self.programming_language = programming_language

    def display_developer_info(self):
        print(f"Developer: {self.name}, Salary: {self.salary}, Language: {self.programming_language}")

dev1 = Developer("srujan", 70000, "Python")

dev1.display_info()           # inherited method
dev1.display_developer_info() # child-specific method

#Multiple-Inheritance:

"""4.Smartphone Features - Class Camera with method take_photo(). - Class MusicPlayer with
 method play_music(). - Class Smartphone (child) inherits from both Camera and MusicPlayer.
"""
class Camera:
    def take_photo(self):
        print("Photo taken!")

class MusicPlayer:
    def play_music(self):
        print("Playing music...")

class Smartphone(Camera, MusicPlayer):
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Smartphone brand: {self.brand}")

phone1 = Smartphone("Samsung")

phone1.show_brand()     
phone1.take_photo()     
phone1.play_music()

"""5.Vehicle Features - Class Engine with method start_engine(). - Class Wheels with method
 rotate_wheels(). - Class Car inherits both and adds drive().
"""
class Engine:
    def start_engine(self):
        print("Engine started!")

class Wheels:
    def rotate_wheels(self):
        print("Wheels are rotating!")

class Car(Engine, Wheels):
    def drive(self):
        print("Car is driving!")

my_car = Car()
my_car.start_engine()  
my_car.rotate_wheels()  
my_car.drive()        

"""6.Hospital Management - Class Doctor with method treat_patient(). - Class Researcher with
 method conduct_research(). - Class DoctorResearcher inherits from both and can do both tasks.
 """
class Doctor:
    def treat_patient(self):
        print("Treating patient...")

class Researcher:
    def conduct_research(self):
        print("Conducting medical research...")

class DoctorResearcher(Doctor, Researcher):
    def show_role(self):
        print("I am a Doctor-Researcher!")

dr_samaram = DoctorResearcher()

dr_samaram.show_role()        
dr_samaram.treat_patient()      
dr_samaram.conduct_research()  

#Multi-Level Inheritance
"""7.Educational Hierarchy - Class Person with attribute name. - Class Teacher inherits Person and
 adds subject. - Class HeadOfDepartment inherits Teacher and adds department_name
"""
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling Person constructor
        self.subject = subject

    def display_teacher_info(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

class HeadOfDepartment(Teacher):
    def __init__(self, name, subject, department_name):
        super().__init__(name, subject)  # call Teacher constructor
        self.department_name = department_name

    def display_hod_info(self):
        print(f"Head of Department:{self.name},Subject:{self.subject},Department:{self.department_name}")

teacher1 = Teacher("Giri", "Mathematics")
teacher1.display_teacher_info()

hod1 = HeadOfDepartment("Sarath", "Physics", "Science")
hod1.display_hod_info()

"""8.Online Shopping System - Product class with attributes name, price. - Electronics class inherits
 Product and adds brand. - Mobile class inherits Electronics and adds ram, storage.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product: {self.name}, Price: {self.price}")

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)  # call Product constructor
        self.brand = brand

    def display_electronics(self):
        print(f"Electronics: {self.name}, Price: {self.price}, Brand: {self.brand}")

class Mobile(Electronics):
    def __init__(self, name, price, brand, ram, storage):
        super().__init__(name, price, brand)  # call Electronics constructor
        self.ram = ram
        self.storage = storage

    def display_mobile(self):
        print(f"Mobile: {self.name}, Brand: {self.brand}, Price: {self.price}, RAM: {self.ram}GB, Storage: {self.storage}GB")

product1 = Product("Ear Buds", 2499)
product1.display_product()

electronic1 = Electronics("Laptop", 50000, "Hp")
electronic1.display_electronics()

mobile1 = Mobile("IQOO",20000, "Z6", 8, 128)
mobile1.display_mobile()

"""
 9. Transport System - Class Vehicle with attribute speed. - Class Car inherits Vehicle and adds
 fuel_type. - Class ElectricCar inherits Car and adds battery_capacity.
"""
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def display_speed(self):
        print(f"Vehicle speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, speed, fuel_type):
        super().__init__(speed)  # call Vehicle constructor
        self.fuel_type = fuel_type

    def display_car(self):
        print(f"Car speed:{self.speed} km/h, Fuel type:{self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, speed, fuel_type, battery_capacity):
        super().__init__(speed, fuel_type)  # call Car constructor
        self.battery_capacity = battery_capacity

    def display_electric_car(self):
        print(f"Electric Car speed:{self.speed} km/h, Fuel type:{self.fuel_type}, Battery:{self.battery_capacity} kWh")


vehicle1 = Vehicle(80)
vehicle1.display_speed()

car1 = Car(120, "Petrol")
car1.display_car()

electric_car1 = ElectricCar(150, "Electric", 75)
electric_car1.display_electric_car()


