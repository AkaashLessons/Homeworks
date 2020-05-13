##recursive procedure that computes the nth fib number
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ..
#fib(0) => 0
#fib(1) => 1
#fib(2) => 1 = 0 + 1
#fib(3) => 2 = 1 + 1
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

##Example and/or

##Example dict problem
def most_common_letter(lis):
    letters = {}
    for word in lis:
        for char in word:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
    max_count = 0
    common_letter = ""
    for key,value in letters.items():
        if value > max_count:
            max_count = value
            common_letter = key
    return(common_letter, max_count)

##Example defining a class - Dog

class Animal:
    def __init__(self, num_arms, num_legs, if_mammal):
        self.num_arms = num_arms
        self.num_legs = num_legs
        self.if_mammal = if_mammal

    def walk(self):
        print("I'm walking!")
        
class Dog(Animal):
    def __init__(self, breed, age, name, owner, num_legs, num_arms, if_mammal):
        self.breed = breed
        self.age = age
        self.name = name
        self.owner = owner
        Animal.__init__(self, num_arms, num_legs, if_mammal)

    def bark(self):
        print("roof!")

    def growl(self):
        print("grrrr")

    def get_older(self):
        self.age += 1

    def change_owner(self,owner):
        self.owner = owner
    


##Problem 1: Write a function that takes in a number and returns True if the number is
# > 5 OR < 10, otherwise it returns False
def between_5_10(number):
    if number < 10 or number > 5:
        return True
    else:
        return False

##Problem 2: Write a function that takes in a string and returns True if the string is
# > 3 letters long AND is uppercase, otherwise it returns false
def string_3_upercase(string):
    if len(string) > 3 and (string).isupper():
        return True
    else:
        return False
##This exercise will build off of itself, so I'll write it in steps
##STEP 1: Define a class to represent a cat
#Cats in general will have names, ages, owners, and colors. Define an __init__
#function in the class to represent these variables
#instancing looks like: Garfield = Cat("Garfield", 41, "Jon Arbunkle", "orange")
##CHALLENGE: also add a variable to represent the number of lives of a cat,
# using default inputs it will be defaulted to 9 lives (haha)
#i.e. Garfield = Cat("Garfield", 41, "jon Arbunkle", "orange", 8)
# Garfield.lives = 8  

##STEP 2: Add a few custom methods to the cat class
# We know cats can purr, hiss, and meow. Write some functions that represent
# these within the class definition
# These will basically just be functions that print "purrrr" or "hissss"
# This will look like: Garfield.purr() => "purrrrr"
# if you did the challenge from above, write a function that decreases their lives


#STEP 3: Change your code (very slightly - doesn't take much) so that Cat class inherits
# from the Animal class we defined earlier
class Cat(Animal):
    def __init__(self,name,age,owner,color,num_legs, num_arms, if_mammal,lives=9):
        self.name = name
        self.age = age
        self.owner = owner
        self.color = color
        self.lives = lives
        Animal.__init__(self, num_arms, num_legs, if_mammal)
    def hiss(self):
        print ("hssssssssssssssssss")

    def pur(self):
        print ("purrrrrrrr")

    def minus_life(self):
        self.lives = self.lives-1

##Step 4: Create a couple instances of cats! Play around with changing their names, ages,
# number of lives, etc. Also try calling the built-in functions

