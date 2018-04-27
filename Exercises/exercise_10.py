"""
Exercise 10 - Generators

For this exercise you will be writing a class for several different generator functions.

1) Write a class called "Gens".
    - This class is initialized with a single integer that is called "start"
    - Include a __str__() method so that when an instance of your class is printed, the returned string includes the value of "start"
        EX: "Start value for generators class is: 5"
    - All generator methods should start at the "start" value, if one is not provided, the class should default to a start value of 1

2) Include in this class, the following methods:
    doubles() - yields number * 2 to infinity, starting at self.start
        Gens(1).doubles() -> 1, 2, 4, 8, 16, ...

    fib() - Yields the next number in the fibonacci sequence to infinity, starting at 1
        Gens(100).fib() -> 1, 1, 2, 3, 5, 8, ...

    linear(n) - yields number + n to infinity, starting at self.start
        Gens(1).linear(2) -> 1, 3, 5, 7, 9, ...

    exponential(n) - yields number raised to the power n to infinity, starting at self.start
        Gens(2).exponential(2) -> 2, 4, 16, 256, ...

    sequence(list) - Ignores starting number, yields one value at a time in the list, looping infinitely many times
        Gens(0).sequence([2, 3, 4]) -> 2, 3, 4, 2, 3, 4, ...

    triple_half() -  Yields a number * 3, then the number / 2, repeating to infinity, starting at self.start
        Gens(2).triple_half() -> 2, 6, 3, 9, 4.5, 13.5, ...

"""
import math

class Gens:

    value = 0;

    def __init__(self, start):
        self.start = start
        self.n1 = 1
        self.n2 = 1

    def __str__(self):
        return "Start value for generators class is: {}".format(self.start)

    def doubles(self):
        print(self)
        while True:
            yield self.start
            self.start = self.start * 2

    def fib(self):
        print(self)
        while True:
            yield self.n1
            self.n1,self.n2 = self.n2,self.n1 + self.n2

    def linear(self, n):
        print(self)
        while True:
            yield self.start
            self.start = self.start + n

    def exponential(self, n):
        print(self)
        while True:
            yield self.start
            self.start = math.pow(self.start, n)

    def sequence(self, list):
        print(self)
        while True:
            for item in list:
                yield item

    def triple_half(self):
        print(self)
        while True:
            yield self.start
            if Gens.value == 0:
                self.start = self.start * 3.0
                Gens.value = 1
            else:
                self.start = self.start / 2.0
                Gens.value = 0

def main():

        d = Gens(1)
        fb = Gens(100)
        lin = Gens(1)
        exp = Gens(2)
        seq = Gens(0)
        th = Gens(2)

        for i in d.doubles():
            if i > 100:
                break;
            else:
               print(i)

        for j in fb.fib():
            if j > 100:
                break;
            else:
                print(j)

        for k in lin.linear(2):
            if k > 10:
                break;
            else:
                print(k)

        for l in exp.exponential(2):
            if l > 50:
                break;
            else:
                print(l)

        counter = 0
        text = seq.sequence([2, 3, 4])
        while counter != 7:
            print(next(text))
            counter += 1

        for i in th.triple_half():
            if i > 20:
                break;
            else:
                print(i)

if __name__ == '__main__':
    main()


