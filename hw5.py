
##recursion
#takes in a number and computes it's factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
def factorial_while(num):
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num = num - 1
    return factorial

def factorial_for(num):
    factorial = 1
    for number in range(1,num+1):
        factorial = factorial*number
    return factorial

#takes in a string and reverses it
def string_reverse(string):
    if len(string) == 1:
        return string
    else:
        return string_reverse(string[1:]) + string[0]

def string_reverse_loop(string):
    return_string = ""
    while len(string) > 0:
        return_string = return_string + string[-1]
        string = string[0:-1]
    return return_string


#takes in a list of numbers and returns the sum of them
def sum_list(lis):
    running_total = 0
    for number in lis:
        running_total = running_total + number
    return running_total

## function to create a new list from a list of numbers
#[2,5,7,4,6,8] => [2,4,6,8]
def divisible_by_2(lis):
    new_list = []
    for number in lis:
        if number%2 == 0:
            new_list.append(number)
    return new_list


##START OF HOMEWORK###
##Problem 1: Create a function that takes a list of strings and returns
#            a new list of the strings that contain the letter 'a'
# Use the format of sum_list and divisible_by_2 as a model
# hint: 'a' is IN string
def a_list(lis):
    new_list = []
    for word in lis:
        if "a" in word:
            new_list.append(word)
    return new_list


##Problem 2: Create a function that takes a list of numbers as input and
#            uses RECURSION to sum the numbers in the list
#            hint: base case is if the list is empty, we'd return 0
def sum_list(lis):
    running_total = 0
    for numer in lis:
        running_total = running_total + number
    return running_total

def sum_list_two(lis):
    if len(lis) == 0:
        return 0
    else:
        return (lis[0]) + sum_list_two(lis[1:])


##Problem 3: Write a function that takes in a list of strings as input
#            and prints each string unless it hits a string that contains
#            the letter 'z', in which case it prints "contains z" doesn't print the string
#            and exits out of the loop
#            hint: what command can we use to BREAK out of a loop
def no_z(lis):
    for string in lis:
        if "z" in string:
            print("contains z")
            break
        print(string)   
##Problem 4: Write a function similar to the one above, but instead of exiting
#            out of the loop, it will print "contains z" if it hits a string
#            with the letter z in it, won't print the string, but will CONTINUE
#            on to the next string in the list
def no_z_cont(lis):
    for string in lis:
        if "z" in string:
            print("contains z")
            continue
        print(string) 
##Problem 5: Write a function that takes in a string as input
#            and outputs the number of unique letters in it (no duplicates)
#            hint: what datatype did we learn that removes duplicates
def unique():
    string = input("please put in a string")
    unique = len(set (string))
    return unique
    
##Problem 6: Try creating a dictionary!
#            For this problem, try to think of things that should be stored in pairs
#            People's names and their ages? A class name and the teacher's name?
#            Look at the slides for the different ways we initialize dicts
#            and create one with 3 pairs in it
#            Then create a function that takes in a dict as input and
#            prints each 'key'
#            hint: use a for loop with <dict>.keys()

ages = {"akaash":14, "anu":22, "ashok":27}
def print_keys(dictionary):
    for key in dictionary.keys():
        print(key)

##create a function called age_10 that adds 10 years to every person's age
def age_10_more(dictionary):
    for key in dictionary.keys():
        dictionary[key] = dictionary[key] + 10
    print(list(dictionary.items()))
##CHALLENGE: Write functions that use iteration (loops - either while or for)
#            for the recursion examples above
# hint: these will look like the sum_list or divisible_by_two problems



