
#Asks the user for a number input and converts it into a int
number = int(input("Enter a number: "))



#It checks to see if the nunber can be divided by 2 and equal 0 by using modulo (%) and then prints the result. 
if number % 2 == 0:
   print("This is an even number")
else:
   print("This is an odd number.")