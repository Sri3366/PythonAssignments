#section-1 using while loop

#1. Print numbers from 1 to 5 using a while loop.
i=1
while i<=5:
    print(i)
    i+=1

#2. Print even numbers from 1 to 10 using a while loop.
print("Even numbers from 1 to 10 are:")
x=1
while x<=10:
    if(x%2==0):
       print(x,end=" ")
    x+=1
print( )

#3. Print the sum of numbers from 1 to 10 using a while loop.

print("sum of numbers from 1 to 10 are:")
i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print(sum)

#4. Print each digit of a number using a while loop.
    #Example: If input is 123, output should be: 1 2 3

num=int(input("Enter the number:"))
list1=[]
while num>0:
    digit=num%10
    list1.append(digit)
    num=(num//10)
for digit in reversed(list1):
    print(digit, end=' ')

 # 5. Print numbers from 10 down to 1 using a while loop.
  
print("10 down to 1")
i=10
while i>0:
    print(i)
    i-=1

#section-2: using for loops

#6.print numbers from 1 to 10 using a for loop
for i in range(1,11):
    print(i)

#7.print each character in the word "Banana" using a for loop 
str="banana"
for i in str:
    print(i)

#8.print the squares of numbers from 1 to 5 using for loop
for i in range(1,6):
    print(i*i)

#9.print all even numbers in the list [2,5,7,9,10]
list=[2,5,7,9,10]
for i in list:
    if i%2==0:
        print(i)

#10.print numbers 1 to 20 that are divisible by 3 using a for loop
for i in range(1,21):
    if i%3==0:
        print(i)

#section-3
#11.print this star pattern using for loop
"""
*
**
***
"""
for i in range(1,4):
    for j in range(1,i-1):
        print(j*"*",end=" ")
    print() 

#12.Print this number pattern using for loop
"""
1 2 3 
1 2 3
1 2 3

"""
for i in range(1,4):
    for j in range(1,4):
        print(j ,end=" ")
    print()

#13.Print the triangle number pattern
"""
1
1 2
1 2 3
"""
for i in range(1,4):
    for j in range(1,i+1):
        print(j ,end=" ")
    print()
#14.print multiplication of 2 table using for loop (10 times)
for i in range(1,11):
    print(f"2 X {i} = ",(2*i)) 

#15.print each character of two words in a list using nested loops
words=["hi","ok"]
for i in words:
    print(f"Characters in '{words}':", end=' ')
    for char in i:
         print(char,end=' ')
    print()

#section-4

#16.print numbers from 1 to 10 and print "Even" or "odd" next to each
for i in range(1,11):
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"odd")

#17.Ask the user to enter 5 numbers and print only the even numbers
list1=[]
for i in range(5):
    num=int(input("enter number:"))
    if num%2==0:
        list1.append(num)
print(list1)

#18.Ask users to enter numbers until they enter a negative number.Then stop
num=0
while num>=0:
    new_num=int(input("Enter a number:"))
    if new_num>=0:
        num=new_num
        print(new_num)
    else:
        num = new_num
        print("Negative number. Stopping the input process.")
    

#19.print vowels in a word using a for loop and if condition
word="hi iam venkat"
vowels=["a","e","i","o","u","A","E","I","O","U"]
for i in word:
    if i in vowels:
        print(i)

#20.count how many vowels are in a given word
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in word:
    if char in vowels:
        vowel_count += 1
print(f"The word '{word}' has {vowel_count} vowels.")
#Section-5  
#21.Print the "HELLO" word 5 times using a loop
a="HELLO"
for i in range(1,6):
    print(a) 
#22.Ask the user their favourite color using 3 times
fav_color=[]
for i in range(1,4):
    color=input("Enter your favourite color:")
    fav_color.append(color)
    print(f"User {i} favourite color is:{fav_color}")

#23.Print the pattern using Nested loop
"""
A
B B
C C C
"""
#method-1
for i in range(3):
    char = chr(65 + i)
    for j in range(i + 1):
        print(char, end=' ')
    print()
#method-2
alpha=["A","B","C"]
for i,char in enumerate(alpha):
    for j in range(i+1):
        print(char,end=" ")
    print()

#24.count how many a letter appears in the word "banana"
word="banana"
count=0
for i in word:
    if i=="a":
        count+=1
print(f"Number of letters in the word banana is:{count}")

#25.print numbers from 1 to 10 .for each print "small" if it's <5 ,else print "Big"
for i in range(1,11):
    if i<5:
        print(i,"Small")
    else:
        print(i,"Big")
