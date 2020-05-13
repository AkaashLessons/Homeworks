##enumerate example
##a function that takes in a list of strings as input
##and if the index of the string is odd, adds an exclamation at the end of the string
##otherwise, adds a period to the end of the string



##zip example
##a function that takes in two lists of numbers as input (A and B, same length)
##and returns a list of the sums where C[i] = A[i] + B[i]


##list comprehension example
##a function that takes in a list of strings as input and
##adds an exclamation at the end of each string that contains a "b"
def excitement(lis):
    return [string + "!" for string in lis if "b" in string]


##map example
##will do the same thing as above but using map
##with two lists as input: will do the same as zip
def add_exclamation(string):
    if "b" in string:
        return string + "!"
    else:
        return string
    
def excitement_map(lis):
    return list(map(add_exclamation, lis))

def add_nums(x,y):
    return x + y

def sum_lists(lis1, lis2):
    return list(map(add_nums, lis1, lis2))


##filter example
##a function that takes in a list of strings as input and
## removes all strings that don't contain the letter "b"
def contains_b(string):
    return "b" in string
def remove_b(lis):
    return list(filter(contains_b, lis))


##########################START OF HOMEWORK#########################

## Problem 1A: Write a function that takes in a list of numbers as input
## and if the sum of the element's index + the element = 10, print out
## "bazinga!", otherwise do nothing (use enumerate)
def bazinga(lis):
    for i,v in enumerate(lis):
        if i + v == 10:
            print("bazinga")
    
##Problem 1B: write a function that does the same thing as above, but
## instead uses zip
#hint: it will still take in 1 list as input, but it will create a list of
#the indices by using range and the length of the list
#(remember to type-cast to a list!)
def bazinga2(lis):
    lis2 = list(range(len(lis)))
    for v,i in zip(lis, lis2):
        if i + v == 10:
            print("bazinga")        
    

##Problem 2A: Write a function that takes in a list of numbers as input
##and returns a list of the numbers in it divisible by 3
## use list comprehension
## hint: divisible by 3 is equivalent to x%3==0
def divisible_by_3(lis):
    new_list = [number for number in lis if number%3==0]
    return new_list


##Problem 2B: write a function that does the same thing as above, but uses map
def map_helper(number):
    if number%3 == 0:
        return number
    
def map_divisible(lis):
    return list(map(map_helper,lis))


##Problem 2C: write a function that does the same as above, but uses filter
def filter_helper(number):
    return number%3==0

def filter_divisible(lis):
    return list(filter(filter_helper,lis))
