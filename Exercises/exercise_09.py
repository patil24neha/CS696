"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math


def time_decorator(my_function):
    def inner_def():
        t0 = time.time()  # capture start time as t0
        result = my_function()
        t1 = time.time()  # capture end time as t1
        print("'{}' finished in {} seconds".format(my_function.__name__, t1 - t0))
        pt = time.process_time()
        print("'{}' finished in {} seconds".format(my_function.__name__, pt))
        size = sys.getsizeof(result)
        print("Size of return value of '{}' is {} ".format(my_function.__name__, size))
        return result
    return inner_def

@time_decorator
def for_loop():
    mylist = []
    for i in range(1 , 1000000):
        mylist.append(i)
    return mylist
for_loop()
# print(for_loop())

@time_decorator
def list_comp():
    return [i for i in range(1 , 1000000)]
list_comp()
# print(list_comp())

@time_decorator
def numpy_list():
    array = numpy.arange(1 , 1000000)
    return array
numpy_list()
# print(numpy_list())

@time_decorator
def pandas_list():
    df = pandas.DataFrame(numpy.arange(1 ,1000000))
    return df
pandas_list()
# print(pandas_list())

@time_decorator
def generator_list():
    list = (i for i in range(1, 1000000))
    for i in list:
        # print(i)
        return i
generator_list()
# print(generator_list())

@time_decorator
def for_loop_log():
    mylist = []
    for i in range(1 , 1000000):
        mylist.append(math.log10(i))
    return mylist
# print(for_loop_log())
for_loop_log()

@time_decorator
def list_com_log():
    return [math.log10(i) for i in range(1, 1000000)]
# print(list_com_log())
list_com_log()

@time_decorator
def numpy_list_log():
    array = numpy.arange(1, 1000000)
    return numpy.log10(array)
numpy_list_log()
# print(numpy_list_log())

@time_decorator
def pandas_list_log():
    df = pandas.DataFrame(numpy.arange(1, 1000000))
    return numpy.log10(df)
# print(pandas_list_log())
pandas_list_log()

@time_decorator
def generator_list_log():
    list = (i for i in range(1, 1000000))
    for i in list:
        # print(numpy.log10(i))
        return numpy.log10(i)
# print(generator_list_log())
generator_list_log()

