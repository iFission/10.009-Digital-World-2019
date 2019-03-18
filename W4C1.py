x = [1, 2, 3]
y1 = [x, 0]
y2 = y1  # both y1 and y2 still aliasing to x
# y2[0][0] = 0
# y2[1] = 1
# y1[0][0]  # (a)
# y1[1]  # (b)
# y2[0][0]  # (c)
# y2[1]  # (d)
# y2[1]  # (d)

# x = [1, 2, 3]
# y1 = [x, 0]
y2 = y1[:]  # both y1 and y2 still aliasing to x
# y2[0][0] = 0
# y2[1] = 1
# y1[0][0]  # (a)
# y1[1]  # (b)
# y2[0][0]  # (c)
# y2[1]  # (d)
# y2[1]  # (d)

# x = [1, 2, 3]
# y1 = [x, 0]
y2 = y1.copy()  # both y1 and y2 still aliasing to x
# y2[0][0] = 0
# y2[1] = 1
# y1[0][0]  # (a)
# y1[1]  # (b)
# y2[0][0]  # (c)
# y2[1]  # (d)
# y2[1]  # (d)

import copy
# x = [1, 2, 3]
# y1 = [x, 0]
y2 = copy.deepcopy(
    y1)  # deep copy forces the nested variables to be copied too
y2[0][0] = 0
# y2[1] = 1
# y1[0][0]  # (a)
# y1[1]  # (b)
# y2[0][0]  # (c)
# y2[1]  # (d)

my_string = 'wander'
my_string.replace('a', 'o')
my_string1 = my_string.replace('a', 'o')
new_string1 = my_string1.replace('a', 'o')

aa = ['Love Live!', 'AKB48', 'KanColle']
aa.sort()
bb = aa.sort()  #this gives None. Why?
bb

a = set('totoro')
print(a)
a.add('p')
print(a)

animals = {'cat': 'meow', 'dog': 'woof', 'rat': 'squeak'}
print(animals.keys(), animals.values(), animals.items())