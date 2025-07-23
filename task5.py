                         #Reusable Functions – Tasks
#task 1..................................
def square_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

sqr = [2, 4, 6, 8, 10]
squared = square_numbers(sqr)
print(squared)

# task 2...............................

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(is_even_or_odd(12)) 
print(is_even_or_odd(9))  



                                #Parameters & Return – Tasks
# task 1..................................
def calculate_area(radius):
    import math
    return math.pi * radius ** 2

print(calculate_area(5)) 

# task 2..................................
def greet_user(name, age):
    return f"Hello {name}, you are {age} years old."

print(greet_user("Zainab", 20))


                                #Scope & Modules – Tasks
# task 1..................................

counter = 0  # Global variable

def change_counter():
    global counter
    counter += 1  

print(counter)       # Output: 0
change_counter()
print(counter)       # Output: 1
change_counter()
print(counter)       # Output: 2

#task 2..................................
import math_tools
result = math_tools.multiply(4, 5)
print("Result:", result)
