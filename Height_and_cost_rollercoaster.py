#Basic user input to ask for height
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
bill = 0


#Checks if they are above 120cm, if they are, then they ask the user for their age and then an if statement is executed. 
if height >= 120:
    print("You're tall enough to ride!")
    age = int(input("What is your age?\n"))

#This is a nested if statement, which is an if statement inside an if statement. There is also an elif, which is just else if.
    if age < 12:
        bill = 5
        print("Children ticket prices are £5")
    elif age <= 18:
        bill = 7
        print("Youth ticket prices are £7")
    else:
        bill = 12
        print("Adult ticket prices are £12")
    
    wants_photo = input("Do you want a photo taken? Y or N\n")
    if wants_photo == "Y":
        #add £3 to their bill
        bill += 3
        print (f"Your total is £{bill}")
    else:
        print(f"Your total is £{bill}")
else:
    print("You're not tall enough to ride.")