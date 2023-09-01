import random

#Generates a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

#Generates a random float between 0.00000 and 0.99999 and multiplies it by 5
random_float = random.random() * 5
print(random_float)

#Same as the first, just displays the result in an F string, similar to the love calculator, just without the names being entered. 
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")