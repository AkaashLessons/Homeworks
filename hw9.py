##This is a review homework! Refer back to the slides, reference doc and other
##homeworks if you need help

##Problem 1: Enumerate
##Write a function that takes in a list of strings as input
##and if the index of the string is odd, adds an exclamation at the end of the string
##otherwise, adds a period to the end of the string
def if_odd(lis):
    for i,v in enumerate(lis):
        if i%2 == 0:
            lis[i] = v + "."
        else:
            lis[i] = v + "!"
    print(lis)


##Problem 2: Zip
##Write a function that takes in two lists of numbers as input (A and B, same length)
##and returns a list of the sums where C[i] = A[i] + B[i]
## for example A = [1,1,1] B = [2,2,2] it will return [3,3,3]
# hint: use ZIP (we already wrote this using map)
def sum_two_lists(lis,lis2):
    lis3 = []
    for a, b in zip(lis,lis2):
        lis3.append(a + b)
    return lis3

##Problem 3: Nested loop
##Write a function that takes in a list of strings (strings that are > 1 word long)
#For each string, SPLIT it into a list of words
#For each word in the list, print out the length
#So we'll need a loop to do the above for every word in our word list
#And then we need a loop to do that for every string in the input list
def multi_split(lis):
    for string in lis:
        word_list = string.split()
        for word in word_list:
            print(len(word))

##Problem 5A: Recursion
##We can determine how many digits a positive integer has by
##repeatedly dividing by 10 (without keeping the remainder) until the
##number is less than 10, consisting of only 1 digit. We add 1 to this
##value for each time we divided by 10. Here is the recursive algorithm:
##          1. If n < 10 return 1.
##          2. Otherwise, return 1 + the number of digits in n/10 (ignoring the fractional part).
##Write a function that takes in a positive integer as input and returns the number of digits
def num_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + num_digits(num/10)

##Problem 5B: While loop
# Do the same as above, but using a while loop.
# hint: we'll store n/10 in a variable and keep dividing this by 10 while the variable > 10,
# keeping a variable that represents the number of digits and adding 1 every time we divide
def while_digits(num):
    digits = 0
    while num >= 10:
        num = num/10
        digits += 1
    return digits + 1

##Problem 5C: Can you think of another way to do the above, but by typecasting the int to a string?
def digits(num):
    return len(str(num))
