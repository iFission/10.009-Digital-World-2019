#%%
5*3 > 10 and 4 + 6 == 11

#%%


def calc_geo(a, r, n):
    return a*(1-r**n)/(1-r)

print(calc_geo(1, 2/3, 10))

#%%
calc_geog = lambda a, r, n: a*(1-r**n)/(1-r)
print(calc_geo(1, 2/3, 10))

#%%
var = 11
def test():
    global var
    var += 1
    print(var)
test()
#%%