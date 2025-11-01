#1."""swap two numbers using a temporary variable and tuple unpacking"""
a=10
b=25
print(f"Before swapping: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")

#2.Identify data types
#Input three values from the user and print their types 
a = input("Enter first value: ")
b = input("Enter second value: ")
c = input("Enter third value: ")

print("Type of first value:", type(a))
print("Type of second value:", type(b))
print("Type of third value:", type(c))

#3. Simple Calculator
#perform +,-.*,/,//,%,** on two numbers based on user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /, //, %, **): ")

if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    print("Result:", num1 / num2)
elif operator == '//':
    print("Result:", num1 // num2)
elif operator == '%':
    print("Result:", num1 % num2)
elif operator == '**':
    print("Result:", num1 ** num2)
else:
    print("Invalid operator!")

#4.
salary = float(input("Enter your current salary: "))
new_salary = salary + (salary * 0.15)
print("Old Salary:", salary)
print("New Salary after 15% hike:", new_salary)

#5.
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
area = pi * radius ** 2
perimeter = 2 * pi * radius
print("Area of the circle:", area)
print("Perimeter (circumference) of the circle:", perimeter)

#6.
char = input("Enter a character: ")
print("ASCII value of", char, "is", ord(char))

#7.
num=int(input("Enter a number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

#8.
x = 10
print("Initial value of x:", x)
x += 5
print("After x += 5:", x)
x -= 3
print("After x -= 3:", x)
x *= 2
print("After x *= 2:", x)
x //= 4
print("After x //= 4:", x)
x %= 3
print("After x %= 3:", x)

#9.Boolean and Logic Check
name = input("Enter your name: ")
age = input("Enter your age: ")

valid_name = len(name) > 0  
age_valid = age.isdigit() and 0 < int(age) < 120  
if valid_name and age_valid:
    print("Both name and age are valid.")
elif not valid_name and not age_valid:
    print("Both name and age are invalid.")
elif not valid_name:
    print("Name is invalid.")
else:
    print("Age is invalid.")

#10.

num = 5  # binary: 0101
print("Original number:", num)
# Left shift by 1 and 2
left_shift_1 = num << 1
left_shift_2 = num << 2
print("Left shift by 1:", left_shift_1)
print("Left shift by 2:", left_shift_2)
# Right shift by 1 and 2
right_shift_1 = num >> 1
right_shift_2 = num >> 2
print("Right shift by 1:", right_shift_1)
print("Right shift by 2:", right_shift_2)

"""
Left Shift (<<)
num << 1 → shift bits left by 1 → 1010 → decimal 10
num << 2 → shift bits left by 2 → 10100 → decimal 20

Right Shift (>>)
num >> 1 → shift bits right by 1 → 0010 → decimal 2
num >> 2 → shift bits right by 2 → 0001 → decimal 1     """

#11.
a = 12  # binary: 1100
b = 5   # binary: 0101
print("a =", a,"binary:",bin(a))
print("b =", b,"binary:",bin(b))
#Bitwise AND
print("a & b =", a & b,"binary:",bin(a & b))
#Bitwise OR
print("a | b =", a | b,"binary:",bin(a | b))
#Bitwise XOR
print("a ^ b =", a ^ b,"binary:",bin(a ^ b))
#Bitwise NOT
print("~a =", ~a, "binary:",bin(~a))
print("~b =", ~b, "binary:",bin(~b))

#12.
s = "25"
i = int(s)
print("String to Integer:", i,"Type:",type(i))
f = 45.67
s2 = str(f)
print("Float to String:", s2,"Type:",type(s2))
n = 0
b = bool(n)
print("Integer to Boolean:", b,"Type:",type(b))

13.
choice =input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius =float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == '2':
    fahrenheit =float(input("Enter temperature in Fahrenheit: "))
    celsius =(fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice!")

#14.
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)
if remainder == 0:
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)
#15
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length of string:", len(text))
word = input("Enter a word to check if it is in the string: ")
if word in text:
    print(f"'{word}' is present in the string.")
else:
    print(f"'{word}' is not present in the string.")

#16.
num = int(input("Enter a 3-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
sum_digits = hundreds + tens + ones
print("Sum of digits:", sum_digits)

#17.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2:",list1 == list2)  # Checks if values are equal
print("list1 is list2:",list1 is list2)  # Checks if both refer to the same object in memory
list3 = list1
print("list1 is list3:",list1 is list3)

#18.
years =int(input("Enter your age in years: "))
months = years * 12
days = years * 365 
print("Age in months:",months)
print("Age in days:",days)

#19.
x = 10 + 3.5
y = "Age:" + str(30)
z = True + False + 2
print("x=", x, "Type:",type(x))
print("y=", y, "Type:",type(y))
print("z=", z, "Type:",type(z))

#20.
n = int(input("Enter a number: "))
neg =~n
left_shift =n<<1
right_shift =n>>2
print("Original number:",n)
print("~n =",neg)
print("n << 1 =",left_shift)
print("n >> 2 =",right_shift)











