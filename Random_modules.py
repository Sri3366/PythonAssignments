#Generate a random float between 0.0 and 1.0.
import random
random_number = random.random()
print("Random float between 0.0 and 1.0:{:.2f}".format(random_number))

#Generate a random integer between 1 and 100. 
import random 
random_integer=random.randint(1,100)
print("Random integer between 1 and 100:",random_integer)

#Pick a random fruit from a list ["apple", "banana", "mango", "orange"]. 
import random
fruits=["apple", "banana", "mango", "orange"]
random_fruit=random.choice(fruits)
print("Randomly selected fruit:",random_fruit)

#Shuffle a list of numbers [1, 2, 3, 4, 5]. 
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

#Generate 5 random integers between 10 and 50
import random
random_numbers = [random.randint(10, 50) for i in range(5)]
print("5 random integers between 10 and 50:", random_numbers)


