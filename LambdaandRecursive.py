#Lambda Functions
"""Write a lambda function to check if a number is even or odd."""
evenorodd=lambda a:"Even" if a%2==0 else "odd"
print(evenorodd(7))

"""Write a lambda function to find the maximum of two numbers"""
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
maxoftwo=lambda x,y:x if x>y else y
print(f"Maximum of Two numbers is:{maxoftwo(x,y)}")

"""Write a lambda function to compute the square of a number."""
square=lambda b:b*b 
print(square(5))

#Intermediate
""" Use map() with a lambda to convert a list of Celsius temperatures to Fahrenheit"""
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c:(c*9/5)+32, celsius))
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

"""Use filter() with a lambda to extract even numbers from a list"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda n: n%2==0, numbers))
print("Original List:", numbers)
print("Even Numbers:", even_numbers)

"""Use reduce() with a lambda to calculate the product of all numbers in a list"""
from functools import reduce 
list1= [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, list1)
print("Numbers:", list1)
print("Product:", product)


