# To print multiple thing with one print all we need to do is seperate them with the help of comma
# \n can only be use with string it help put string in the next line 
# Printing multiple items with one print statement using comma separation
print("hello how you doing", type("hello how you doing"))

# String concatenation to concatenate strings
print("hello" + " how you doing" + " I am doing good")

# Assigning a value to a variable
a = 2
print(a)

# Boolean comparisons
print(10 > 11)
print(10 > 5)

# Logical AND operator
print(10 > 5 and 5 > 99)
print(10 > 5 and 100 == 100)

# Logical OR operator
print(10 > 5 or 5 > 99)

# Using if statement to check a condition
a = 10
if a > 0:
    print("Yes, a is greater than 0")

# Using if-else statement
var1 = 100
if var1 > 10:
    print(var1, "is greater than 10")
else:
    print(var1, "is smaller than or equal to 10")

# Using if-elif-else statement to check multiple conditions
a = 10
if a < 5:
    print(a, "is smaller than 5")
elif a < 7:
    print(a, "is smaller than 7")
elif a > 9:
    print(a, "is greater than 9")
else:
    print("None of the conditions are met")
