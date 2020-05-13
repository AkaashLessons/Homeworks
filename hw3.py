##function that takes in a list of numbers and prints the sum of 10 + each number in the list
def add_10(nums):
    for num in nums:
        print(num + 10)


##returns the output of x+y AND x-y
def add_subtract_x_y(x,y):
    return x + y, x-y

##returns the output of x + y
def add_x_y(x,y):
    return x + y

##return different strings based on the result of add_x_y on two input numbers
def if_test(x, y):
    num = add_x_y(x,y)
    if num > 10:
        return "wow!"
    elif num < 2:
        return "yikes"
    else:
        return "cool"

########START OF HOMEWORK##########

##Problem 1: Write a function that takes in a string and returns the first letter if the length of the string > 10
    ## returns the second letter if the length of the string < 5
    ## and returns "empty!!" if the length of the string is 0


##Problem 2: Write a function that takes in a list of numbers. If there are more the list contains more than 3 1's, return "tricycle"
    #if there are no 1's return "goose egg". Otherwise, return "middle of the road"

##Problem 3: Write a function that takes in a list of strings and for each string prints out whether it's uppercase or not
    
