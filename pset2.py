# pset 2 cohort

#%%
# 1 #
def position_velocity(v0, t):
    '''CS1 - Position Velocity'''
    g = 9.81
    return round(v0*t - 1/2 * g * t**2, 2), round(v0 - g*t,2)

print(position_velocity(5.0, 10.0))
print(position_velocity(5.0, 0.0))
print(position_velocity(0.0, 5.0))

#%%
# 2 #
def bmi(weight, height):
    '''CS2 - BMI'''
    return round((weight / ((height/100))**2) ,1)

print(bmi(60,120))
print(bmi(50,150))
print(bmi(43.5,142.3))

my_weight = float(input("Weight in kilograms: "))
my_height = float(input("Height in centimetres: "))
print("BMI: {bmi}".format(bmi = bmi(my_weight, my_height)))
#%%
# 3 #
from math import sqrt

class Coordinate:
    x = 0.0
    y = 0.0

def area_of_triangle(p1, p2, p3):
    side1 = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    side2 = sqrt((p3.x-p2.x)**2 + (p3.y-p2.y)**2)
    side3 = sqrt((p1.x-p3.x)**2 + (p1.y-p3.y)**2)
    s = (side1 + side2 + side3)/2
    return round(sqrt(s*(s-side1)*(s-side2)*(s-side3)), 2)


p1 = Coordinate()
p1.x = float(input("Enter x coordinate of the first point of a triangle: "))
p1.y = float(input("Enter y coordinate of the first point of a triangle: "))
p2 = Coordinate()
p2.x = float(input("Enter x coordinate of the second point of a triangle: "))
p2.y = float(input("Enter y coordinate of the second point of a triangle: "))
p3 = Coordinate()
p3.x = float(input("Enter x coordinate of the third point of a triangle: "))
p3.y = float(input("Enter y coordinate of the third point of a triangle: "))
ans = area_of_triangle(p1, p2, p3)
print("The area of the triangle is {area}".format(area = ans))

#%%
# 5 #

def describe_bmi(bmi):
    if bmi >= 27.5:
        print('high risk')
        return 'high risk'
    elif bmi >= 23:
        print('moderate risk')
        return 'moderate risk'
    elif bmi >= 18.5:
        print('low risk')
        return 'low risk'
    else:
        return 'nutritional deficiency'

#%%
# 6 #

def letter_grade(mark):
    if mark < 0 or mark > 100:
        return None
    elif mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'E'

#%%
# 7 #


class Coordinate:
    x = 0.0
    y = 0.0


def is_in_square(square1, side1, square2, side2):
    s1_x_lower = square1.x - side1
    s1_x_upper = square1.x + side1
    s1_y_lower = square1.y - side1
    s1_y_upper = square1.y + side1

    s2_x_lower = square2.x - side2
    s2_x_upper = square2.x + side2
    s2_y_lower = square2.y - side2
    s2_y_upper = square2.y + side2

    # test if edge 1 of square2 is in square 1
    if (s2_x_lower >= s1_x_lower and s2_x_lower <= s1_x_upper) and (s2_y_upper >= s1_y_lower and s2_y_upper <= s1_y_upper):
        return True
    # test if edge 2 of square2 is in square 1
    elif (s2_x_upper >= s1_x_lower and s2_x_upper <= s1_x_upper) and (s2_y_upper >= s1_y_lower and s2_y_upper <= s1_y_upper):
        return True
    # test if edge 3 of square2 is in square 1
    elif (s2_x_upper >= s1_x_lower and s2_x_upper <= s1_x_upper) and (s2_y_lower >= s1_y_lower and s2_y_lower <= s1_y_upper):
        return True
    # test if edge 4 of square2 is in square 1
    elif (s2_x_lower >= s1_x_lower and s2_x_lower <= s1_x_upper) and (s2_y_lower >= s1_y_lower and s2_y_lower <= s1_y_upper):
        return True
    else:
        return False


s1 = Coordinate()
s1.x, s1.y = 10, 10
s2 = Coordinate()
s2.x, s2.y = 20, 20
print(is_in_square(s1, 1, s2, 1))


# pset 2 homework
#%%
# 1 #
fahrenheit_to_celsius = lambda F: (F-32) / 9*5
print(fahrenheit_to_celsius(-40))

#%%
# 2 #
celsius_to_fahrenheit = lambda C: C * 9/5 + 32
print(celsius_to_fahrenheit(0))

#%%
# 3 #
from math import pi
def area_vol_cylinder(radius, length):
    area = radius * radius * pi
    vol = area * length
    return round(area,2), round(vol,2)

area_vol_cylinder(1.0,2.0)

#%%
# 4


def wind_chill_temp(temp, speed):
    return (35.74) + (0.6215*temp) - (35.75 * speed**0.16) + (0.4275 * temp * speed**0.16)


print(wind_chill_temp(5.3, 6))
#%%
# 5


def minutes_to_years_days(minutes):
    days = minutes / (1440)
    return int(days // 365), int(days % 365)


print(minutes_to_years_days(1000000000))
#%%
# 6
def minutes_to_years_days(minutes):
    pass

def investment_val(amt, rate, years):
    return round(amt * (1+rate/100/12) ** (years*12), 2)

# print(investment_val(1000, 4.25, 1))

import unittest

class Testing(unittest.TestCase):
    def test_investment(self):
        a = investment_val(1000, 4.25, 1)
        b = 1043.34
        self.assertEqual(a, b)

unittest.main()

#%%
# 7 #


def is_larger(n1, n2):
    return n1 > n2


#%%
# 8 #
def check_value(n1, n2, n3, x):
    return x > n1 and x > n2 and x < n3


check_value(1, 4, 8, 7)
