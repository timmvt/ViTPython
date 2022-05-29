# # modules are packages of built in functions and variables and/or classes that make it easier to use

# # these modules are loaded into your code using the import statement, as shown yesterday (and again in a few minutes)

# # continuing from the previous recipe analogy, think of a module as a cookbook that contains recipes for common tasks

# # the math cookbook has recipes for common math tasks
# # the django cookbook has recipes for common django tasks (web development)
# # the sql cookbook has recipes for common sql tasks
# # etc.


# #--------------IMPORTING MODULES---------
# #Use the "import" keyword to bring outside functions/programs into the file you are currently working on.  For example, to add additional math functionality to your file, import the "math" module.
# import math

# #Now you can use math functions that were not previously available, like:

# # num1 = math.sqrt(16)
# # print("num1 is ", num1)

# # num2 = math.pi
# # print("num2 is ", num2)

# # tip = math.sinh(num2)
# # print(tip)



# ### --------- Exercise -----------
# # 
# # 1) import the math module
# #
# # 2) create a function that takes in a number parameter and returns the square root of that number
# # 
# # 3) create another function that takes in 3 parameters, multiplies them together, and then returns the result of that multiplication and the square root of the result
# # 
# # 
# # 4) create a function that takes in a number parameter and returns the sine of that number
# #
# #
# ### ---------- Exercise ----------- 

# # using the random module


# ******TESTING********

# import exercise  # or exercise.py
# import math

# three_param(3, 3, 3)
import random
import math
from random import randrange

# This code needs work!
def random_number():
    rand_num = int(input('please give me the first of two numbers, low and high: \n'))
    rand_num2 = int(input('please give me the second of two numbers, low and high: \n'))
    # x = float(input("Pick any number: \n"))
    print('Random number: ' + str(randrange(rand_num,rand_num2)))
    # random.seed(x)
    
    print('Random seed: ' + str(random.random()))

random_number()

# SEED

