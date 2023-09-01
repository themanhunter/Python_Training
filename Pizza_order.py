print("Hello, welcome to Freddy Faz Bear's pizzeria!")

#Asks for size of pizza using letters for small, medium or large
size = input("What size pizza do you want? S, M or L? \n")


#Sets the current bill at 0
bill = 0


#Checks to see what letter they put, depending on the size, the bill is increased.
if size == "S":
    bill = 15
    print("A small pizza is £15")

elif size == "M":
    bill = 20
    print("A medium pizza is £20")

else:
     bill = 25


#Asks if they want any extra pepperoni using Y and N, if they do, and depending on the size of the pizza, the bill is increased. if not,
#Then it moves on to extra cheese
add_pepperoni = input("Do you want extra pepperoni? Y or N \n")

if add_pepperoni == "Y":
     if size == "S":
           bill += 2
     else: 
          bill += 3


#Asks if they want extra cheese, if they do the bill is increased by 1 and then the bill amount is printed using an F string. 
extra_cheese = input("Would you like extra cheese? Y or N \n")
if extra_cheese == "Y":
     bill += 1
     print(f"Your final bill is £{bill}")

#This is triggered if at any point they chose N for either cheese or pepperoni, and the bill is printed based on their order.
else:
     print(f"Your final bill is £{bill}")




    
    



