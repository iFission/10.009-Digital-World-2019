#%%
'cohort1'

from math import sqrt


class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


#%%
'cohort2'


class Celsius:
    def __init__(self, temp=0):
        self.temperature = temp

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # is called when trying to retrieve the value of temperature
    def get_temperature(self):
        print('getting value')
        return self._temperature  # the temperature is a private property, different from self.temperature

    # is called when trying to change the value of temperature
    def set_temperature(self, value):
        if value < -273:
            print("Temperature below -273 is not possible")
            self._temperature = -273
        else:
            print('setting value')
            self._temperature = value

    temperature = property(
        get_temperature,
        set_temperature)  # var has to match the name of the attribute

    temp1 = property(get_temperature, set_temperature)


#%%
'cohort3'

import time


class StopWatch():
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1

    def start(self):
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        return round(self.end_time - self.start_time,
                     1) if self.end_time != -1 else None


#%%
'cohort4'
import numpy as np


class Line():
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return self.c0 + self.c1 * x

    def table(self, L, R, n):
        if n == 0:
            return "Error in printing table"
        n = 1 if L == R else n
        x_list = np.linspace(
            L, R, n)  # use np linear space method to generate x_list
        y_list = np.vectorize(self.__call__)(
            x_list)  # vectorise __call__ method, calc y_list
        table = ''
        for x, y in zip(x_list, y_list):
            table += (
                f'{x:10.2f}{y:10.2f}\n')  # {variable:{width}{float precision}}
        return table


#%%
'hw1'


class Time():
    def __init__(self, h, m, s):
        self._hours = h
        self._minutes = m
        self._seconds = s

    def __str__(self):
        return f'Time:{self._hours:2}:{self._minutes:2}:{self._seconds:2}'

    @property
    def elapsed_time(self):
        return self._hours * 60 * 60 + self._minutes * 60 + self._seconds

    @elapsed_time.setter
    def elapsed_time(self, elapse):
        print(elapse)
        self._elapsed_time = elapse
        self._hours = self._elapsed_time // (60 * 60) % 24
        self._minutes = self._elapsed_time // 60 % 60
        self._seconds = self._elapsed_time % 60
        return self.elapsed_time


#%%
'hw2'


class Account:
    """docstring for Account"""

    def __init__(self, owner, account_number, amount):

        self._owner = owner
        self._account_number = account_number
        self._balance = amount

    def __str__(self):
        return f'{self._owner}, {self._account_number}, balance: {self._balance}'

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


#%%
'hw3'


class Diff():
    def __init__(self, f, h=1e-4):
        self._f = f
        self._h = h

    def __call__(self, x):
        return (self._f(x + self._h) - self._f(x)) / self._h


#%%
'hw4'
from itertools import zip_longest
import numpy as np


class Polynomial(object):
    def __init__(self, coeff):
        self.coeff = [int(x) for x in coeff]
        # always convert to int, account for auto-float in np's polynomial class

    def __add__(self, poly):
        return Polynomial([
            x + y for x, y in zip_longest(self.coeff, poly.coeff, fillvalue=0)
        ])
        # uses zip_longest to zip 2 lists of different lengths together, fill the shorter list with 0

    def __sub__(self, poly):
        return Polynomial([
            x - y for x, y in zip_longest(self.coeff, poly.coeff, fillvalue=0)
        ])

    def __mul__(self, poly):
        return Polynomial(
            list((np.polynomial.Polynomial(self.coeff) *
                  np.polynomial.Polynomial(poly.coeff))))
        # uses np's polynomial class, has built in multiplication method
        # stores as float
        # stores powers in increasing order
        # np.poly1d stores in decreasing order

    def __call__(self, x):
        return self.evaluate(x)

    def evaluate(self, x):
        sum = 0
        power = 0
        for coeff in self.coeff:
            sum += x**power * coeff
            power += 1
        return sum

    def differentiate(self):
        self.coeff = self.derivative().coeff

    def derivative(self):
        diff_coeff = []
        power = 1
        for coeff in self.coeff[1:]:
            # print(coeff, power)
            diff_coeff.append(coeff * power)
            power += 1
        return Polynomial(diff_coeff)