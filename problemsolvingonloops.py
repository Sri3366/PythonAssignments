#1.Print Reverse of a string without built-in functions
str=input("Enter your string:")
reversed_str=str[::-1]
print(f"Reversed string:{reversed_str}")

#using for loop
def reversed_string(s):
    reverse_s=""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s
my_string=input("Enter the string:")
result=reversed_string(my_string)
print(f"Reversed string:{result}")

#2.Average of marks of five students
        #marks=[400,450,530,550,570]

marks=[400,450,530,550,570]
sum=0
for i in marks:
    sum+=i
avg=sum/len(marks)
print(avg)

#3.check whether the given sides form a triangle or not a=5,b=5,c=5
"""(Triangle Rule:Sum of any two sides is greater than the third side)"""
a=b=c=5
if a > 0 and b > 0 and c > 0:
    check_ab = (a + b > c)
    check_ac = (a + c > b)
    check_bc = (b + c > a)
    if (check_ab and check_ac and check_bc)==True:
        print("Result: YES, the given sides form a triangle.")
    else:
        print("Result: NO, the given sides DO NOT form a triangle.")