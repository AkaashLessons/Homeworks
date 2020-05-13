import random ##we need this to use the random module

##an example that uses input (uncomment it to see it in action)
#name = input("Please put your name: ")
#print("Hello " + name)


##Problem 1: Write a function that doesn't take in any arguments, but asks the user
# to pick a number and prints that number^3
##hint: we will need to use type-casting (make the user input a number!)
def pick_a_number():
    number = int(input("please put in a number: "))
    return number**3

    
##Problem 2: Write a function that takes in a list of length 5 and returns a random element
# from the list
##challenge: make it take in a list of any length!
def randomize(lis):
    randomize = lis[random.randint(0,4)]
    return randomize
def randomize(lis):
    randomize = lis[random.randint(0,len(lis)-1)]
    return randomize
 
##Problem 3: Write a function that adds two numbers together
# if you call it with 2 numbers it will add them together
# if you call it with only 1 number it will default to adding 10 to it
def add(number):
    lenth =  len(number)
    if lenth == 1:
        return number[0] + 10
    elif lenth == 2:
        return sum(number)
    else:
        return "nothing"

def add_two(x, y=10):
    return x + y

##Problem 4: Write a function that doesn't take in any arguments
# it will ask the user to input a number
# if the number > 5, it will output "greater"
# if the number < 5, it will output "less"
# otherwise, it will output "equal!"
def is_it_5():
    number = int(input("please put in a number: "))
    if number > 5:
        return "greater"
    elif number < 5:
        return "less"
    else:
        return "equal!"
#Problem 5: write a function that takes in a list of strings
# for each string, if the string has the letter 'a' in it print "4.0"
# otherwise, print "no As"
def a_in_it(lis):
    for word in lis:
        if 'a' in word:
            print("4.0")
        else:
            print("no As")


##Problem 6: Write a function that prints the numbers 0-10 backwards
#challenge: try to do this with both a for loop and while loop
def backwards():
    counter = 10
    while counter > 0:
        print(counter)
        counter = counter - 1

def backwards():
    for num in reversed(list(range(11))):
        print(num)


##Problem 7: Write a function that takes in a list of strings and outputs the sum
# of the length of the strings
def sum_length_list(lis):
    running_total = 0
    for word in lis:
        running_total = running_total + len(word)
    return running_total
##example for problem 7 that implements the functionality of the sum function
#takes in a list of numbers and returns the sum of them
def sum_list(lis):
    running_total = 0
    for number in lis:
        running_total = running_total + number
    return running_total















