print("Welcome to the tip calculator")

#Asks for the bill, and converts it into a float, because it can end with a decimal place 
total = input("What is your total bill?\n£")
actual_total = float(total)

#Asks for the tip, which is calculated by dividing the number by 100, so 12 would become 0.12
#The total is the multiplied by the tip and then added to get the final total
tip = input("What tip percentage would you like to give?\n")
tip_percentage = float(tip) / 100
tip_calculation = actual_total * tip_percentage
final_total = actual_total + tip_calculation

#Asks how many people you want to split the bill between, and then divides the total by that amount. 
#It then formats the amount to 2 decimal places, as bills are written out to 2 decimal places.
people = input("How many people to split the bill?\n")
actual_people = int(people)
amount_each = final_total / actual_people
formatted_amount = format(amount_each, '.2f')

#Prints out the final amount using an F string. 
print(f"Each person should pay £{formatted_amount}")
