import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
            '^', '_', '`', '{', '|', '}', '~']


print("Welcome to Pypassword_list generator!")

nr_letters = int(input("How many letters would you like in your password_list?\n"))
nr_numbers = int(input("How many numbers would you like in your password_list?\n"))
nr_symbols = int(input("How many symbols would you like in your password_list?\n"))

#Easy level

# password_list = ""

# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password_list += random_char
#     print(password_list)

# for num in range(1, nr_numbers +1):
#     random_num = random.choice(numbers)
#     password_list += random_num
#     print(password_list)

# for sym in range(1, nr_symbols + 1):
#     random_sym = random.choice(symbols)
#     password_list += random_sym
#     print(password_list)

# Hard level

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for num in range(1, nr_numbers +1):
    password_list.append(random.choice(numbers))

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
    password += char

print(f"You password is {password}")