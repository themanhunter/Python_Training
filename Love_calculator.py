print("Welcome to the love calculator")

#Asks for both peoples names
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

#Combines both names into one, and turns all the characters into lowercase
combined_string = name1 + name2
lower_case_string = combined_string.lower()



#Checks the amount of times t,r,u,e,l,o and v appear in the names provided and then adds them together into true and love 
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v  = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e




#True and love are converted from int's to str's and saved as the true_love variable, this is to instead of adding them together as on whole
#number, it puts them side by side as a number.
true_love = int(str(true) + str(love))




#Checks to see if the number is inbetween one of the ranges, and will then print out the result depending on the number.
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos")

elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together")

else:
    print(f"Your score is {true_love}")






