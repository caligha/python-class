print("hello, world")

#  var
name = "Alice"

mylist = [1, "hello", 3.14, True, name, [0, 1, 2, [3, 4, 5,]]]
mytuple = (1, "hello", 3.14, True, name, [0, 1, 2, [3, 4, 5,]])
myDict =  {
    "name" : "Alice",
    "number" : "2142541631",
    "email" : "alice@gmail.com"
}

print(type(mylist))
print(mylist)
print(mylist  [5])
print(mylist  [5][3])
print(mylist  [5][3][2])

mylist[3] =False 
print(mylist)
# mytuple[3] =False 
# print(mytuple)

# User input
name = input("Enter your name: ")
print(name)

# conditional statement allow your program make decision basi
# we can also use 
# logical operators: and,(both need to pass) or (one of the condition had to pass), not reverse the sitution
age = int(input("enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# loop we have for loop and while  loop
num = 0
while num < 5:
    print(num)
    num += 1
   
   
    
print()
print()
 
for m in  range(5):
    print(m)
    
    
print()
print()
    
mylist =[1, 2, 3, 4, 5]
for i  in mylist:
    print(i)

# functions are reusable blocks of  code that perform  a specific task. you can define your own functions using th def keyword.
def  greet(name):
    return "hello, "+   name + "!"

print(greet("name"))

def  sound(animal):
    return "meow"


def attribute(animal):
    return "I'm a " + animal + " !, my sound is " +  sound(animal)
print(attribute("animal"))


# we can also add string together
firstname =  "john"
surname  = "dou"

fullname = firstname + surname
print(fullname)