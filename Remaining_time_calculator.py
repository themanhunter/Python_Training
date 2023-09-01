#Calculating the maximum days, weeks and months you have left if you live until 90
max_age_months = 90 * 12
max_age_weeks = 90 * 52
max_age_days = 90 * 365


#user inputs age here
age = input("What is your current age?\n")


#converts the the result of age from a string into an integer and saves as a variable for each
month_result = int(age) * 12
weeks_result = int(age) * 52
days_result = int(age) * 365


#Calcualting what you have left
months_left = max_age_months - month_result
weeks_left = max_age_weeks - weeks_result
days_left = max_age_days - days_result


#Using an F string to allow concatination for all the results
print(f"You have {months_left} months {weeks_left} weeks {days_left} days left")