import numpy as np
import math

def mean(x):
    sum = 0
    # calculate and return the mean of a numpy array
    for i in range(len(x)):
        sum += x[i]
    return sum/len(x)

def median(x):
    tmp = sorted(x)
    return tmp[len(x)//2] if len(x) % 2 == 1 else (tmp[len(x) // 2] + tmp[(len(x) //2)-1]) / 2

def spread(x):
    return max(x) - min(x)

def vars(x):
    ([(x - mean(xs)) ** 2 for i in xs])
    
def std(xs):
    return math.sqrt(vars(xs))

# something you will see...
# we can maeke this do the print, but *only* as the 
# standalone program, not through an import
# when a python varibale runs, it sets the dunder __name__
# variable to be its context in the greater program
# So the program that got ran through python is __main__
# typically used if you want to have some tests here but
# DONT RUN THE TESTS WHEN YOU IMPORT THIS INTO OTHER PROGRAMS