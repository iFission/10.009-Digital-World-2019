#%%
# cohort2
def compound_value_months(amt, rate, months):
    monthly_deposit = amt
    rate_monthly = rate / 12
    for month in range(months):
        amt = amt * (1 + rate_monthly)
        if month < months - 1:
            amt += monthly_deposit
    return round(amt, 2)


#%%˙
# cohort3
def sum_list(ls):
    sum = 0
    for n in ls:
        sum += n
    return sum


def find_average(lst):
    list_avg = []
    running_sum = 0
    running_numbers_tally = 0
    list_inner_avg = []
    for list_inner in lst:
        # print(list_inner)
        if len(list_inner) == 0:
            list_inner_avg.append(0.0)
        else:
            running_numbers_tally += len(list_inner)
            temp = sum_list(list_inner) / len(list_inner)
            running_sum += sum_list(list_inner)
            # print(type(temp))
            list_inner_avg.append(temp)
    list_avg.append(list_inner_avg)
    # print(running_sum, running_numbers_tally)
    list_avg.append(running_sum / running_numbers_tally)
    average = running_sum / running_numbers_tally
    return list_inner_avg, average


find_average([[13.13, 1.1, 1.1], [], [1, 1, 0.67]])

#%%
# cohort4


def transpose_matrix(matrix):
    return [[row[column] for row in matrix]
            for column in range(len(matrix[0]))]


assert transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7],
                                                               [2, 5, 8],
                                                               [3, 6, 9]]

#%%
# cohort5


def get_details(name, key, list):
    for mydict in list:
        print(mydict)
        if name in mydict.values():
            if key in mydict.keys():
                return mydict[key]
    return None


phonebook = [{
    'name': 'Andrew',
    'mobile_phone': 9477865,
    ' office_phone': 6612345,
    'email': 'andrew@sutd.edu.sg'
},
             {
                 'name': 'Bobby',
                 'mobile_phone': 8123498,
                 'office_phone': 6654321,
                 'email': ' bobby@sutd.edu.sg'
             }]
print(get_details('Bobby', 'office_phone', phonebook))


#%%
# cohort 6
def get_base_counts(seq):
    if len(seq):
        dict_seq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for base in seq:
            if base in dict_seq.keys():
                dict_seq[base] += 1
            else:
                return "The input DNA string is invalid"
        return dict_seq
    else:
        return "The input DNA string is invalid"


get_base_counts('AaCaGT')
#%%
# hw1
f_to_c = lambda F: (F - 32) / 9 * 5
f_to_c_approx = lambda F: (F - 30) / 2


def get_conversion_table():
    table = []

    for F in range(0, 100 + 1, 10):
        table.append([F, round(f_to_c(F), 1), round(f_to_c_approx(F), 1)])
    return table


def transpose_table(lst):
    return [[row[column] for row in lst] for column in range(len(lst[0]))]


print(get_conversion_table())
print(transpose_table(get_conversion_table()))

#%%
# hw2


def max_in_list(ls):
    if len(ls) == 0:
        return None
    max = ls[0]
    for n in ls[1:]:
        if n > max:
            max = n
    return max


def max_list(inlist):
    outlist = []
    for ls in inlist:
        outlist.append(max_in_list(ls))
    return outlist


assert max_list([[1, 2, 3], [4, 5]]) == [3, 5]


#%%
# hw3
def multiplication_table(n):
    return None if n < 1 else [[row * column for row in range(1, n + 1)]
                               for column in range(1, n + 1)]


multiplication_table((1))


#%%
# hw4
def most_frequent(lst):
    freq_dict = {}
    for i in lst:
        if i in freq_dict.keys():
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    freq_i = []

    max_freq = 0

    for i, freq in freq_dict.items():
        if freq > max_freq:
            freq_i = []
            max_freq = freq
            freq_i.append(i)
        elif freq == max_freq:
            freq_i.append(i)
    return freq_i


most_frequent([9, 30, 3, 9, 3, 2, 4])


#%%
# hw5
def diff(polynomial):
    dict_diff = {}
    for indice, power in polynomial.items():
        if indice >= 1:
            dict_diff[indice - 1] = indice * power
    return dict_diff


diff({1: -3, 3: 2, 5: -1, 6: 2})
