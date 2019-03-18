#%%
# cohort1
def reverse(st):
    st_r = ''
    for c in st:
        st_r = c + st_r
    return st_r


st1 = "I am testing"
print(reverse(st1))


#%%
# cohort2
def check_password(passwd):
    lett = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    if len(passwd) < 8:
        return False

    # checks passwd only contain lett and num
    for chr in passwd:
        if chr not in lett and chr not in num:
            return False

    # check passwd contains at least 2 digits
    num_count = sum(chr in num for chr in passwd)

    return True if num_count >= 2 else False


passwd = '1123123oT22'
print(check_password(passwd))


#%%
# cohort3
def longest_common_prefix(str1, str2):
    str = ''
    for chr1, chr2 in zip(str1, str2):
        if chr1 == chr2:
            str += chr1
        else:
            break
    return str


longest_common_prefix('distanc', 'disinfection')

#%%
# cohort4
from math import sqrt
import sys


class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.mag = self.magnitude()

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)


def extract_values(string):
    # print(string.split())
    m, n = [float(x) for x in string.split('\t')]  # can't return directly
    # return (int(x) for x in string.split()) gives <generator object extract_values.<locals>.<genexpr> at 0x10b579048>
    # altertavite
    # m, n = map(int, string.split())
    return m, n


def get_maxmin_mag(f):
    pmin, pmax = Coordinate(), Coordinate()
    max1 = sys.float_info.min
    min1 = sys.float_info.max
    for line in f.readlines():
        x, y = extract_values(line)
        p = Coordinate(x, y)  # instantiate p as a new Coordinate object
        if p.mag > max1:
            pmax.x, pmax.y = x, y
            max1 = p.mag
        elif p.mag < min1:
            pmin.x, pmin.y = x, y
            min1 = p.mag

    return pmax, pmin


f = open('week6/text_files/xy.dat', 'r')

pmax, pmin = get_maxmin_mag(f)
print(f'max: ({pmax.x:f}, {pmax.y:f})')
print(f'min: ({pmin.x:f}, {pmin.y:f})')


#%%
# hw1
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for i in str(binary)[::-1]:
        decimal += int(i) * 2**power
        power += 1
    return decimal


binary_to_decimal('101')

#%%
# hw2
import re


def uncompress(string):
    out_string = ''
    nums = re.finditer('\d+', string)
    # uses regular expression (import re)
    # usage:
    # re.finditer('paratemer', string)
    # returns an iterator of <re.Match object; span=(0, 1), match='2'>
    # parameter, \d searches for all digits
    # parameter + indicates match 1 or more times, to account for double-digit number, eg 12
    # index of start, end+1 of the matched string = .span()
    # matched string = .group()
    for num in nums:
        out_string += string[num.span()[1]] * int(num.group())
        # string[num.span()[1]] gives the letter immediately after matched digit
        # multiply by the number of times as matched in digit, need to convert the str to int
    return out_string


uncompress('2a5b1c192d')

#%%
# hw3
import re


def get_base_counts2(seq):
    # check if the complementary set from A-Z is found in seq , if found, return false
    if re.findall('[^A-Z]', seq) != []:
        return "The input DNA string is invalid"

    dict_seq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    match = re.findall('[A, C, G, T]',
                       seq)  # create a match object, list of matched bases
    for base in dict_seq.keys():
        dict_seq[base] = match.count(
            base)  # count the number of occurences of the base, assign to dict
    return dict_seq


get_base_counts2('CcCCCCGGT')

#%%
# hw4
f = open('week6/text_files/constants.txt', 'r')


def get_fundamental_constants(f):
    out_dict = {}
    for line in f.readlines(-1):
        line = line.split()
        if len(line) == 3:
            out_dict[line[0]] = float(line[1])
    return out_dict


get_fundamental_constants(f)['gravitationalconstant']
#%%
# hw5
f = open('week6/text_files/scores.txt', 'r')


def list_sum(ls):
    sum = 0
    for n in ls:
        sum += n
    return sum


def process_scores(f):
    ls = [float(i) for i in f.read().split()]
    return list_sum(ls), list_sum(ls) / len(ls)


process_scores(f)
