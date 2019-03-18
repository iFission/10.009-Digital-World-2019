n = 5
while n > 1:
    if n%2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    print(n)
#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x,y)

#%%
import matplotlib.pyplot as plt
from math import exp

def f(x): return 1/(1+exp(-x))

x_list = list(np.linspace(-5,5,50))
y_list = [f(x) for x in x_list]

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_list, y_list)
ax.scatter(x_list, y_list)
ax.set_title('Logistic Function')
ax.set_xlabel('x values')
ax.set_ylabel('y values')