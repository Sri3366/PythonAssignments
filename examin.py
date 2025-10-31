#1.Write a python program to print the all numbers between 1 and 100 that are divisible by 3 or 5 but not both
for i in range(1,101):
    if (i%3==0 or i%5==0) and not (i%3==0 and i%5==0):
            print(i)

#2.Write a program to find the second largest number in a list without using sorting or built-in functions
#like max() or sorted()
def find_second_largest(numbers):
     if len(numbers) < 2:
          return None

     largest = second_largest = float('-inf')
     for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

     if second_largest == float('-inf'):
          return None

     return second_largest
nums = [10, 5, 8, 20, 15]
result = find_second_largest(nums)
print("Second largest number is:", result)

#3.Write a program that checks whether a string is a palindrome or not(same forward and backward)ignoring spaces,punctuatins and cases

string = "mom"
if string == string[::-1]:
     print(string,"is a palindrome")
else:
     print("Not a Palindrome")


#4.write a program to print this pattern
def pyramid(n):
     for i in range(1,n+1):
          for j in range(6-i):
               print(" ",end=' ')
          for k in range(1,2*i):
               print("*",end='')
          print()
pyramid(5)
     
#5.write a python program that finds the greatest common divisor (GCD) of two numbers without using the math module
a=int(input("Enter the first integer:"))
b=int(input("Enter the second integer:"))
def gcd(a,b):
     while b!=0:
          temp=b
          b=a%b
          a=temp
     return a
print(f"gcd of {a} and {b} is:",gcd(a,b))

#6.write a program that takes a list of integers and prints a new list containing only prime numbers from it.
def prime(n):
     if n < 2:
        return False
     for i in range(2, int(n ** 0.5) + 1):
          if n % i == 0:
            return False
     return True
numbers = [2, 3, 4, 5, 10, 11, 13, 15, 17, 20]
prime_numbers = [num for num in numbers if prime(num)]
print("Prime numbers in the list:", prime_numbers)

#7.Write a program to count the frequency of each word in a given sentence and print the results as a dictionary
sentence = "Hello world. This is a simple test. Hello again, world!"
cleaned_sentence = sentence.lower()
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for char in punctuation:
     cleaned_sentence=cleaned_sentence.replace(char," ")
     words = cleaned_sentence.split()

     word_counts = {}

     for i in words:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1

print(f"Original sentence: \"{sentence}\"\n")
print("Word frequencies:")
print(word_counts)

#8.Write a program to generate the list of the first N Prime numbers (Where N is given by the user)
n=int(input("enter the prime number upto which u require:"))
if n <= 0:
     print("\nInvalid input. Please enter a positive integer.")
else:
     primes = [] 
     num = 2     
     while len(primes) < n:
               is_prime = True  # Assuming the current number is prime.
                
               if num > 1:
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break  
               else:
                    is_prime = False
  
               if is_prime:
                    primes.append(num)
               num += 1
            
     print(f"\nThe first {n} prime numbers are:")
     print(primes)


#9.Write a python progrm that takes a list of integers and prints all pairs of numbers whose sum is equal to a given target
#(Example:List=[2,4,3,7,5],Target=7 --> Output:[(2,5),(4,3)]) 
list=[2,3,4,5,7,6]
pair=[]
target=7
for i in range(len(list)):
     for j in range(i+1,len(list)): #For accessing next element
          if list[i]+list[j]==target:
               pair.append((list[i],list[j]))
print(f"Pairs with a sum of {target} are: {pair}")

#10.A number is called an Armstrong number if the sum of its digits raised to the power of the number of the digits is equal to the number itself.
#Example:153=1^3+5^3+3^3 Now write  a program to check whether a number entered by an user is an armstrong or not.
def armstrong(n):
    original = n
    digitcount = 0
    temp = n
    while temp > 0:
        temp = temp // 10
        digitcount += 1

    armsum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        power = 1
        for i in range(digitcount):
            power *= digit
        armsum += power
        temp = temp // 10

    return armsum == original


number =int(input("Enter any number to check armstrong or not:"))
if armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")




#Secod metod for gcd using built in
'''
Step 1:
Divide 54/24.
54=2 x 24 + 6
The remainder is 6. 
The problem is now to find the GCD of 24 and 6.

Step 2:
Divide 24/6.
24=4 x 6 + 0
The remainder is 0. Since the remainder is zero, the algorithm stops. The GCD is the last non-zero remainder, which is 6.

Therefore, the greatest common divisor of 54 and 24 is 6.'''
import math
def calculategcd(num1,num2):
     return math.gcd(a,b)
print(calculategcd(56,24))









                
