#%%
# cohort1
import random

craps = set([2, 3, 12])
naturals = set([7, 11])


def roll_two_dices():
    return random.randint(1, 6), random.randint(1, 6)


def print_lose():
    print('You lose')


def print_win():
    print('You win')


def print_point(p):
    print(f'Your points are {p}')


def is_craps(n):
    return n in craps


def is_naturals(n):
    return n in naturals


# ATTENTION!
# You shouldn't need to edit the function below


def play_craps():
    point = -1
    while True:
        n1, n2 = roll_two_dices()
        sumn = n1 + n2
        print('You rolled %d + %d = %d' %
              (n1, n2, sumn))  #initial points obtained here
        if point == -1:  #At the initialisation of point == -1 (see line 29)
            if is_craps(sumn):  #if the sum is in the set of craps
                print_lose()  #then it is an immediate loss
                return 0
            elif is_naturals(sumn):  #if the sum is in the set of naturals
                print_win()  #then it is an immediate  win
                return 1
            point = sumn
            print_point(point)
        else:
            if sumn == 7:
                print_lose()
                return 0
            elif sumn == point:
                print_win()
                return 1  #goal of the game is to keep rolling dice until the sum == points obtained


play_craps()


#%%
# cohort2
def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


print(leap_year(2012))


#%%
def R(x, y):
    return x % y


def day_of_week_jan1(year):
    if year >= 1800 and year <= 2099:
        A = year
        return R(1 + 5 * R(A - 1, 4) + 4 * R(A - 1, 100) + 6 * R(A - 1, 400),
                 7)


print(day_of_week_jan1(2019))


#%%
def num_days_in_month(month_num, leap_year):
    month_normal = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    month_leap = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if leap_year:
        return month_leap[month_num]
    else:
        return month_normal[month_num]


print(num_days_in_month(2, False))


#%%
def construct_week(first_day, day_week, nb_days):
    # inputs: date of first day of the week, date of the week for the first week (0-Sun, 6-Sat), number of days
    week = ''  # empty string for the week
    # print full week, missing_days == 0
    # print 3 spaces for every missing day
    missing_days = ' ' * 3 * day_week
    week = week + missing_days
    for i in range(nb_days):
        cur_date = first_day + i
        cur_day = f'{cur_date:3}'
        week += cur_day
    return week


construct_week(27, 0, 7)


#%%
def print_cal_month(list_of_str):
    ret_val = ''
    for l in list_of_str:
        ret_val += l.replace(' ', '*')
        ret_val += '\n'
    return ret_val


def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    if (month_num >= 1 or month_num <= 12) and (first_day_of_month >= 0
                                                or first_day_of_month <= 6):
        cal_month = []
        cal_month.append(month[month_num])

        week_day = first_day_of_month
        first_day_of_week = 1
        while first_day_of_week <= num_days_in_month:
            days_current_week = 7 - week_day
            days_left_in_month = num_days_in_month - first_day_of_week + 1
            if days_current_week > days_left_in_month:
                days_current_week = days_left_in_month
            # print(week_day, days_current_week)
            cur_week = construct_week(first_day_of_week, week_day,
                                      days_current_week)
            cal_month.append(cur_week)
            first_day_of_week += days_current_week
            week_day = 0
        return cal_month


print(construct_cal_month(2, 1, 28))


#%%
def construct_cal_year(year):
    cal_year = []
    cal_year.append(year)
    leap = leap_year(year)
    first_day_of_month = day_of_week_jan1(year)
    for month in range(1, 12 + 1):
        days_in_month = num_days_in_month(month, leap)
        # print(days_in_month)
        cal_year.append(
            construct_cal_month(month, first_day_of_month, days_in_month))
        first_day_of_month = (first_day_of_month + days_in_month % 7) % 7
        # print(first_day_of_month)
    # print(cal_year)
    return cal_year


print(construct_cal_year(2018))


#%%
def print_space_display_calendar(calendar):
    temp = calendar.replace(' ', '*')
    return temp.replace('\n', '+\n')


def display_month(calendar, month):
    month_str = ''
    month_str += f'{month[0]}\n'
    month_str += f'  S  M  T  W  T  F  S\n'
    for week in month[1:]:
        month_str += f'{week}\n'
    month_str += '\n'
    return month_str


def display_calendar(year):
    calendar = construct_cal_year(year)
    cal_str = ''
    for month in calendar[1:]:
        cal_str = cal_str + display_month(calendar, month)
    return cal_str[:-2]


print(print_space_display_calendar((display_calendar(2015))))
print(len(print_space_display_calendar((display_calendar(2015)))))


#%%
# cohort3
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return fact_rec
    (n - 1) * n


fact_rec(4)


#%%
# hw1
def get_data():
    return input("Enter integer pair:\n")


def extract_values(string):
    print(string.split())
    m, n = [int(x) for x in string.split()]  # can't return directly
    # return (int(x) for x in string.split()) gives <generator object extract_values.<locals>.<genexpr> at 0x10b579048>
    # altertavite
    # m, n = map(int, string.split())
    return m, n


#%%
def calc_ratios(x):
    if x[1] == 0:
        return None
    return x[1] / x[0]


calc_ratios((134, 289))


#%%
# hw2
def display_month(calendar, month):
    if type(month) == int:
        month = calendar[month - 1]
    month_str = ''
    month_str += f'{month[0]}\n'
    month_str += f'  S  M  T  W  T  F  S\n'
    for week in month[1:]:
        month_str += f'{week}\n'
    month_str += '\n'
    return month_str


def display_calendar_modified(year, month):
    calendar = construct_cal_year(year)
    if month == None:
        cal_str = ''
        for month in calendar[1:]:
            cal_str = cal_str + display_month(calendar, month)
        return cal_str[:-2]
    else:
        return display_month(calendar, month + 1)[:-2]


display_calendar_modified(2019, None)
