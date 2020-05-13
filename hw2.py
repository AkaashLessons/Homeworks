##here are the 2 functions we wrote in class##
##we didn't go over this, but instead of writing print at the end of the function
##write return which accomplishes the same thing but will be more useful later
def three(number):
    return number + 3

def a_to_b(a_word):
    b_word = a_word.replace('a','b')
    return b_word

#Problem 1: write a function that takes in an float and returns a int
#example: takes in 2.9, returns 2

def float_to_int(flo):
    integer = int(flo)
    return integer

#Problem 2: write a function that takes in a temp in Fahrenheit and returns it in celsius
#hint 1: the input and outputs will be numbers
#hint 2: the conversion formula is C = (F - 32) x 5/9
#example (use this to check that you got it right): takes in 44, returns 6.6666667

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

 
#Problem 3: write a function that takes in a string and returns the first two letters followed by "poop"
#example: takes in "hello", returns "hepoop"

def poop(word):
    poop = word[0:2] + "poop"
    return poop
    

#Problem 4: write a function that takes in a list and returns a list of the third element repeated 4 times
#example 1: takes in ["akaash", "can", "do", "this"], returns ["do, "do", "do", "do"]
#example 2: takes in [1, 2, 3, 4], returns [3, 3, 3, 3]

def repeat(lst):
    repeat = lst[2:3] * 4
    return repeat


#Problem 5: write a function that takes in a string and checks whether the letter "a" is in it
#example: takes in "alphabet", returns True
#hint: use the "in" method

def a_in_it(string):
    a_in_it = "a" in string
    return a_in_it

def a_in_it(string, letter):
    a_in_it = letter in string
    return a_in_it

 
