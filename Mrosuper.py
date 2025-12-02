#1.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)  # call parent constructor
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()  # reuse parent method
        print(f"Programming Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)  # call parent constructor
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")

dev = Developer("Venkat", 440, "Python")
mgr = Manager("sri", 420, 8)

print("Developer Details:")
dev.display_details()

print("\nManager Details:")
mgr.display_details()

#2.
import math
class Shape:
    def area(self):
        print("Area method must be implemented in the subclass.")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        result = self.length * self.breadth
        print(f"Area of Rectangle: {result} sq.units")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi *(self.radius**2)
        print(f"Area of Circle:{result:.2f} sq.units")

rect = Rectangle(10, 5)
circle = Circle(7)

rect.area()
circle.area()

#3.
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)  # call parent constructor
        self.doors = doors

    def display_info(self):
        super().display()  # reuse parent method
        print(f"Number of Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def display_info(self):
        super().display()
        print(f"Type of Bike: {self.bike_type}")

car1 = Car("Toyota", 2022, 4)
bike1 = Bike("Yamaha", 2023, "Sports")

print("Car Information:")
car1.display()

print("\nBike Information:")
bike1.display()

#4.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)  # call parent constructor
        self.student_id = student_id
        self.course = course

    def display_student(self):
        self.display_person()
        print(f"Student ID: {self.student_id}, Course: {self.course}")

class Sports:
    def __init__(self, sport_name):
        self.sport_name = sport_name

    def display_sports(self):
        print(f"Sports Activity: {self.sport_name}")

class CollegeStudent(Student, Sports):
    def __init__(self, name, age, student_id, course, sport_name):
        Student.__init__(self, name, age, student_id, course)  # from Student(Person)
        Sports.__init__(self, sport_name)  # from Sports

    def display_details(self):
        self.display_student()
        self.display_sports()

college_student = CollegeStudent("Sri venkat", 22, "440", "Electronics and communication", "Basketball")

print("College Student Details:")
college_student.display_details()

#5.
class Staff:
    def __init__(self, name):
        self.name = name

    def display_staff(self):
        print(f"Staff Name: {self.name}")

class Teacher(Staff):
    def __init__(self, name, subject):
        Staff.__init__(self, name)
        self.subject = subject

    def display_teacher(self):
        print(f"Subject: {self.subject}")

class Researcher(Staff):
    def __init__(self, name, research_area):
        Staff.__init__(self, name)
        self.research_area = research_area

    def display_researcher(self):
        print(f"Research Area: {self.research_area}")

class Professor(Teacher, Researcher):
    def __init__(self, name, subject, research_area, publications):
        Teacher.__init__(self, name, subject)
        Researcher.__init__(self, name, research_area)
        self.publications = publications

    def display_professor(self):
        self.display_staff()
        self.display_teacher()
        self.display_researcher()
        print(f"Publications: {self.publications}")

# Example usage
prof = Professor("Dr. Smith", "Physics", "Quantum Mechanics", 25)
print("Professor Details:")
prof.display_professor()


#6.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product Name: {self.name}")
        print(f"Price: Rs.{self.price}")

class Electronics(Product):
    def __init__(self, name, price, brand):
        Product.__init__(self, name, price)  # call Product constructor directly
        self.brand = brand

    def display_electronics(self):
        print(f"Brand: {self.brand}")

class Accessories(Product):
    def __init__(self, name, price, warranty):
        Product.__init__(self, name, price)
        self.warranty = warranty

    def display_accessories(self):
        print(f"Warranty: {self.warranty} years")

class Smartphone(Electronics, Accessories):
    def __init__(self, name, price, brand, warranty, storage):
        Electronics.__init__(self, name, price, brand)
        Accessories.__init__(self, name, price, warranty)
        self.storage = storage

    def display_smartphone(self):
        print("=== Smartphone Details ===")
        self.display_product()
        self.display_electronics()
        self.display_accessories()
        print(f"Storage: {self.storage} GB")

# Example usage
phone = Smartphone("Galaxy S25", 79999, "Samsung", 2, 256)
phone.display_smartphone()


#7.
class Fee:
    def calculate(self, base_fee):
        print(f"Base fee: Rs.{base_fee}")
        return base_fee

class TuitionFee(Fee):
    def calculate(self, base_fee):
        # Call parent method using super()
        total = super().calculate(base_fee)
        # Add tuition-related charges
        extra_charges = 5000
        total += extra_charges
        print(f"Added tuition charges: Rs.{extra_charges}")
        print(f"Total tuition fee: Rs.{total}")
        return total

tuition = TuitionFee()
tuition.calculate(20000)

#8.
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)  # Call base deposit
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: Rs.{interest:.2f}. Balance after interest: Rs.{self.balance:.2f}")

# Testing
acc = SavingsAccount("SA123", 1000)
acc.deposit(500)

#9.
class A:
    def show(self):
        print("Inside A's show()")

class B(A):
    def show(self):
        print("Inside B's show()")
        super().show()  # Call parent (A) method

class C(B):
    def show(self):
        print("Inside C's show()")
        super().show()  # Call parent (B) method

# Testing
obj = C()
obj.show()

#10.
""" Diamond Problem: Class A → method display(). Classes B(A) and C(A) override display().
 Class D(B, C) → no display(). Check which method executes (D → B → C → A).   """

class A:
    def display(self):
        print("madharaasi")

class B(A):
    def display(self):
        print("Animal Instinct")

class C(A):
    def display(self):
        print("Don't Touch")

class D(B, C):
    pass  # No display() defined here

# Testing
obj = D()
obj.display()

# Check Method Resolution Order
print("MRO of class D:", [cls.__name__ for cls in D.__mro__])

#11.
class A:
    def show(self):
        print("Inside A's show()")

class B(A):
    def show(self):
        print("Inside B's show()")

class C(A):
    def show(self):
        print("Inside C's show()")

class D(B, C):
    pass  # No show() defined here

# Testing
obj = D()
obj.show()  # Which show() will be called?

# Print Method Resolution Order
print("MRO of class D:", [cls.__name__ for cls in D.__mro__])

#12
class Book:
    def info(self):
        print("This is a book")

class EBook(Book):
    def info(self):
        print("This is an E-Book")

class AudioBook(Book):
    def info(self):
        print("This is an Audio Book")

class DigitalLibrary(EBook, AudioBook):
    pass  # No info() defined here

# Testing
library_item = DigitalLibrary()
library_item.info()  # Which info() will be called?

# Check Method Resolution Order
print("MRO of DigitalLibrary:", [cls.__name__ for cls in DigitalLibrary.__mro__])


