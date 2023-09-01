#Simple function
def my_function():
    print("Hello")
    print("Bye")
my_function()


#Function that allows for input
def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do you do {name}?")
greet_with_name("man_hunter")


#Function with more than 1 input (Arguments can be specified at the start or when it's called)
def greet_with(name = "man_hunter", location = "REDACTED"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("man_hunter", "Redacted")