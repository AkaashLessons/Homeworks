##The following problems have pieces of written code with the desciprtion for what the function
##is supposed to do. Each problem will have 1 OR MORE issues that you have to fix.
##Either before or after fixing them, write unittest test cases for each function in tests.py.
##It's important that you RUN this homework so you can see what is outputted right now because
##that will help you fix the functions and make sure your new code works.
##If you get stuck, think about how you would write your code to solve the problem before seeing
##broken code

##PROBLEM 1
##function that takes in a list of numbers and removes all the negative numbers
## [5,4,-1,-6,3,0,-7] => [5,4,3,0]
def pos_number(x):
    return x > 0

def only_positivees(lis):
    return map(pos_number,lis)


##PROBLEM 2
##function that takes in a list of strings as input
# it first asks the user for a word
# loops through the list printing the strings out
# but if the string starts with the same letter as the user's, skip it
def first_letter(lis):
    user = input("please put in a word: ")
    for word in lis:
        if word[0] == user[0]:
            break
        else:
            return word

##PROBLEM 3
##function that takes in a string as input and changes the second letter to "p"
def second_letter_p(word):
    word[1] = "p"
    return word

##PROBLEM 4
##function that takes in two lists as input and creates a dictionary from the lists
##the items from the first list should be the keys and the items from the second the values
##lists_to_dict(["strawberries", "clementines", "bananas"], ["red", "orange", "yellow"])
##              => {"strawberries":"red", "clementines":"orange", "bananas":"yellow"}
def lists_to_dict(keys, values):
    Dict = {}
    for key,value in zip(keys,values):
        Dict.append(key) = value
    return Dict


##PROBLEM 5
##function that takes in a list and returns the sum
##the different inputs we have to consider are:
##  1. empty list, i.e recursive_sum([]) => 0
##  2. list of numbers, i.e recursive_sum([1,5,2,3]) => 11
##  3. nested list of numbers, i.e recusrive_sum([1, 2, [3,4], [6, [0,2]]]) => 18
def recursive_sum(nums):
    if nums == []:
        return 0
    else:
        if type(nums[0]) != list:
            return nums[0] + nums[1:]
        else:
            return recursive_sum(nums[0]) + recursive_sum(nums[1:])


##PROBLEM 6
##function that takes in a list of strings as input and writes each string to a file
##we want EVERY string in the file
def write_list(lis):
    for string in lis:
        f = open("output.txt", "w")
        f.write(string + "\n")
    f.close()


    

        
            
