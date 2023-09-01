import random

print("Welcome to banker roulette")

#Asks for a list of people, split with a comma
names_string = input("Give me everybody's names, seperated by a comma.\n")


#Takes names_string and uses .split to split all the names inputted between the commas 
names = names_string.split(",")

#num_items is equal to the length of the names inputted
num_items = len(names)


#Using .randint, it specifies to choose a number between 0 and num_items(which is the amount of names in the list) -1, because lists start at 0
random_choice = random.randint[0, num_items - 1]


#Person_to_pay is then equal to the names we inputted, but also using the random choice we just used, it then prints the name that the random 
# choice has selected, determined by the number generated, and what person is equal to that number on the list.
person_to_pay = names[random_choice]
print(person_to_pay + " is going to pay today")