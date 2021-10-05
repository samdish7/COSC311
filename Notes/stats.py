import numpy as np
import math

def mean(x):
    """calculate and return the mean of a numpy array"""
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum/len(x)


def median(x):
    """return the 'middle value' of the array x after sorting"""
    tmp = sorted(x)
    # use // for integer division (i.e. round down)
    return tmp[len(x) // 2] if len(x) % 2 == 1 else (tmp[len(x) // 2] + tmp[(len(x) // 2)-1]) / 2

def spread(x):
    """one way to measure the spread of data"""
    return max(x) - min(x)

def var(xs):
    """return variance of x -- the average squared distance from the mean"""
    return mean([(x - mean(xs))**2 for x in xs])

def std(xs):
    return math.sqrt(var(xs))

def cov(xs, ys):
    """Take two lists of observations and compute their covarience"""
    return mean([(x - mean(xs))**2 for x in xs])

def correlation(xs, ys):
    """calculate the (Pearson) correlation coefficent"""
    pass

# something you will see...
# we can make this do the print, but *only* when this
# file is run as a standalone program, not through an import.
# when a python program runs, it sets the dunder __name__ 
# variable to be its context in the greater program.
# So the program that got ran through python is __main__
# typically used if you want have some tests here but 
# don't run the tests when you import into other programs
if __name__ == '__main__':
    print('testing stats.py...')
    
    print(f'the mean of [1,2,3,4,5] is {mean(np.array([1,2,3,4,5]))}')
    # assert(mean(np.array([1,2,3,4,5])) == 3.5)
    
    print(f'the median of [2,5,4,3,1] is {median([2,5,4,3,1])}')
    
    print(f'the median of [2,5,4,3] is {median([2,5,4,3])}')
    
    print(f'the variance of [2,5,4,3] is {var([2,5,4,3])}')
    
    print(f'the standard deviation of [2,5,4,3] is {std([2,5,4,3])}')