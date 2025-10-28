job=True
money=True
skills=True
if(job==True and money==True and skills==True):
    print("neeku enti bro balisinodivi")
elif job==True:
    print("Go to job")
elif money==True:
    print("start a business")
elif skills==True:
    print("Do a FreeLance")
else:
    print("join coaching center")

#write a program whether to order a coffe or tea or water based on the money you have
money=int(input("Enter the money u have:"))
if money>=100:
    print("ek coffee")
elif money<100 and money>20:
    print("oka chai")
else:
    print("paani dedho bhai")

#write a program to check whether a person is eligible to vote or not
age=int(input("enter your age:"))
if age>18:
    print("you are eligible to vote")
else:
    print("you are ineligible")

#write a program to assign a grade based on the percentage a student got
percentage=int(input("Enter your Percentage:"))
if percentage>=90:
    print("o Grade")
elif percentage>=80:
    print("A Grade")
elif percentage>=70:
    print("B Grade")
elif percentage>=60:
    print("C Grade")
elif percentage>=50:
    print("D Grade")
else:
    print("Fail")


#write a python program for traffic signal 
signal="red"
if signal=="green":
    print("Go")
elif signal=="yellow":
    print("Wait")
else:
    print("stop")


#write a  python program for login System
username=input("Enter the Username:")
password=input("password:")
if username=="Venkat" and password=="Venkatv@3":
    print("Login Successful")
else:
    print("Invalid Credentials")

#check if a number is divisible by both 3 and 5
number=int(input("Enter a non-negative number:"))
if number%3==0 and number%5==0:
    print("Divisible by both 3 and 5")
elif number%3==0:
    print("divisible by 3")
elif number%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 3 and 5")

#compare two numbers and print which one is greater
num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
if num1>num2:
    print("num1 is greater than num2")
else:
    print("num2 is greater than num 1")

#check if a number is positive and even
number=int(input("Enter the number:"))
if  number>0 and number%2==0:
    print("positive and even number")
elif number<0:
    print("Negative number")
else:
    print("odd number")

#Ask the users age and suggest
age=int(input("Enter your age:"))
if age<13:
    print("child:budatha")
elif age>=13 and age<=19:
    print("u are in nibba-nibbi stage")
else:
    print("Em undhi le inka")


age=int(input("Enter your age:"))
if(age>=18):
    license=input("Do u have License:")
    if(license=="yes"):
        print("Eligible to drive")
    else:
        print("Go and Get licence")
else:
    print("minor")


marks=int(input("enter your marks:"))
if marks>=35:
    if marks>=90:
        print("you got o Grade")
    elif marks>=75:
        print("you got A Grade")
    elif marks>=65:
        print("you got B Grade")
    elif marks>=45:
        print("You got C Grade")
    else:
        print("You got D Grade")
else:
    print("you failed")

'''check if a number is positive in first if-else and the number is even or not in second if-else
 and the number is greater than 50 in third if-else'''

num=int(input("Enter the number:"))
if num>=0:
    print("Your number is positive")
    if(num%2==0):
        print("your number is even number")
    else:
        print("odd number")
        if num>50:
            print("your number is greater than 50")
        else:
            print("Your number is below 50")
else:
    print("Your number is negative")


#check for driving license using and
age=int(input("Enter your age:"))
license=input("Do u have License:")
if age>=18 and license=="yes":
     print("Eligible to drive")
elif age<=18:
    print("you are minor")
else:
    print("Go and Get licence")
