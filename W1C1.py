#%%
print("Hello, world")

#%%
x = 18.0

#%%
O_O = (16//5)+1%(6-4)
O_O

#%% geometric series
def calc_geo(a, r, n):
    return a*(1-r**n)/(1-r)

print(calc_geo(1,2/3, 10))

#%%
a = '''nsaotehu
aoeusnthe'''
id(a)