"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse

def compute(**kwargs):
    flag = True
    try:
        if type(kwargs['input']) is list:
            for i in kwargs['input']:
                if not isinstance(i,int):
                    flag = False
                    print("Input is not a list of integers")
                    break

            if flag is True:
                if kwargs['action'] == 'sum':
                        if kwargs['return_float'] is True:
                            print(float(sum(kwargs['input'])))
                        else:
                            print(sum(kwargs['input']))

                elif kwargs['action'] == 'mean':
                        if kwargs['return_float'] is True:
                            print(float(sum(kwargs['input'])) / len(kwargs['input']))
                        else:
                            print(sum(kwargs['input']) / len(kwargs['input']))
        else:
            print("Input is not a list of integers")
    except:
        print("Input is not a list of integers")
    return

compute(input=[0,1,2,3], action='sum',return_float=True)
compute(input=[0,1,2,3], action='mean',return_float=True)
compute(input=[0,1,2,3], action='sum',return_float=False)
compute(input=[0,1,2,3], action='mean',return_float=False)
compute(input=[0,1,2,'l'], action='mean',return_float=False)
compute(input=234, action='mean',return_float=False)
compute(input='234', action='mean',return_float=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='It allows user to use command line arguments to run the script')
    parser.add_argument('-m', '--multiply', help='This mulltiply each value by the value of -m and print the result', type=int)
    parser.add_argument('-s', '--sum', help='It prints the sum of all arguments', action='store_true')
    parser.add_argument('remainder', help='It containes the arguments used for Sum and Multiply operation', nargs=argparse.REMAINDER)


    try:
        args = parser.parse_args()
        s = args.sum
        multiply = args.multiply
        remainder = args.remainder

        if s is True:
            print(sum(int(i) for i in remainder))
        else:
            for i in remainder:
                print(multiply*int(i))

    except:
        parser.print_help()
        sys.exit(1)
