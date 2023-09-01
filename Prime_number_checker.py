def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            print("This is not a prime number")
    if is_prime:
        print("This is a prime number")



n = int(input("Check this number: "))
prime_checker(number = n)