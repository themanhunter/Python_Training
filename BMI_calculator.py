#Asks user for weight and height input and converts them into floats.
Weight = float(input("What is your weight in Kg?\n"))
Height = float(input("What is your height in meters?\n"))

#This uses the round function to round the result to the nearest whole number, also calculates the BMI.
BMI = round(Weight / Height ** 2)

#Uses if and elif statements to output the results, is also uses f strings to allow floats and ints to be displayed.
if  BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you are overweight")
elif BMI <=35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")
