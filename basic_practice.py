# Variable ans Date Types:

# Declare three variables: num1 (an integer), num2 (a float), and name (a string).
num1 = 10
num2 = 3.5
name = "Chiamaka"

# Print the values and types of these variables.

print(num1, type(num1))
print(num2, type(num2))
print(name, type(name))


# User input
# Prompt the user to enter their age.
age = int(input("Enter your age: "))


# Print a message based on the age:
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
# Conditional Statements:
# Write a function named check_number that takes an integer parameter num.
def check_number(num):
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")
        
    
# Call this function with different integer values to test it.
check_number(0)
check_number(-4)
check_number(2)


# Loops:

# Write a loop that prints all even numbers from 0 to 20 (inclusive).
print("Even numbers from 0 to 20:")
for i in range(0, 21, 2):
    print(i)


# Write a function named calculate_circle_area that takes a single parameter radius (a float).
def calculate_circle_area(radius):
    # Calculate the area of a circle using the formula: area = pi * radius^2
    pi = 3.14
    area = pi * radius ** 2
    return area

# Call this function with different values of radius and print the results.
print("Area of a circle with radius 2:", calculate_circle_area(2))
print("Area of a circle with radius 3.5:", calculate_circle_area(3.5))