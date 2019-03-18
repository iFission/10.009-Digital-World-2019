#%%
# CS1
def list_sum(ls):
    sum = 0
    for n in ls:
        sum += n
    return sum


list_sum([4.25, 5.0, 10.75])

#%%
# list np
import numpy as np


def list_sum(ls):
    return np.dot(np.array(ls), np.ones(len(ls)))


list_sum([4.25, 5.0, 10.75])
#%%
np.ones(5)


#%%
# CS2
def minmax_in_list(ls):
    if len(ls) == 0:
        return None, None
    min = ls[0]
    max = ls[0]
    for n in ls[1:]:
        if n < min:
            min = n
        if n > max:
            max = n
    return min, max


minmax_in_list([3, 3, 3])


#%%
# CS3
def is_palindrome(num):
    num = str(num)
    # print(num, len(num), type(num))
    if len(num) > 1:
        # print('more than 1')
        if num[0] == num[-1]:
            # print(num[1:-1])
            return is_palindrome(num[1:-1])
        else:
            return False
    return True


print(is_palindrome('231231231232'))

#%%


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


print(is_palindrome('232'))


#%%
def is_palindrome(num):
    num = str(num)
    if len(num) < 2:
        return True
    if num[0] != num[-1]:
        return False
    return is_palindrome((num[1:-1]))


print(is_palindrome('231'))


#%%
# CS3
def is_palindrome(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i - 1] == num[-i]:
            pass
        else:
            return False
    return True


print(is_palindrome(12343211))


#%%
# HW1
def fahrenheit_to_celsius(F):
    return (F - 32) / 9 * 5


def celsius_to_fahrenheit(C):
    return C * 9 / 5 + 32


def temp_convert(choice, temp):
    if choice == 'F':
        return celsius_to_fahrenheit(temp)
    elif choice == 'C':
        return fahrenheit_to_celsius(temp)
    else:
        return None


temp_convert("C", 32)


#%%
# HW2
def get_even_list(ls):
    list = []
    for n in ls:
        if n % 2 == 0:
            list.append(n)
    return list


get_even_list([11, 21, 31, 41, 51])


#%%
# HW3
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


is_prime(21)

#%%
# HW4
from math import exp
import numpy as np


def approx_ode(h, t0, y0, tn):
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    y = y0
    t = t0
    for t in np.arange(t0, tn, h):
        print(t)
        y = y + h * (3 + exp(-t) - 1 / 2 * y)
    return y


approx_ode(0.1, 0, 1, 5)

# approx_ode(0.1, 0, 1, 0)


#%%
# jose
def approx_ode(h, t0, y0, tn):
    from math import exp
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    func = lambda t, y: 3 + exp(-t) - (y / 2)
    #yn=y0
    while abs(t0 - tn) > 1e-10:
        print(t0)
        yn = y0 + h * func(t0, y0)
        t0 += h
        y0 = yn
    return y0


approx_ode(0.1, 0, 1, 5)
#%%
# jiawei
import math


def approx_ode(h, t0, y0, tn):
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    i = 0
    loop = (tn - t0) / h
    print(loop)
    ynext = y0
    t = t0
    while i < loop:
        ynext1 = ynext + h * (3 + math.exp(-t) - 0.5 * ynext)
        ynext = ynext1
        t = t + h
        i += 1
    return ynext


approx_ode(0.1, 0, 1, 5)

#%%
import numpy as np
print([n for n in np.arange(0, 5, 0.1)])
