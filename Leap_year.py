year = int(input("Which year do you want to check?\n"))


#Checks to see if the remainder (which is what % does, and is called modulo) of the year, when divided by 4, 100 
# and 400 is equal to 0 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("not a leap year")
    