from random import random
from math import sqrt
import matplotlib.pyplot as plt
import math
PI = math.pi

hits = 0

yy = []
x_ = []


for xx in range(1,10000):
    x_.append(xx)
    hits = 0
    for i in range(1,xx):
        x , y = random(), random()
        dist = sqrt (x**2 + y**2)
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits/xx)
    yy.append(abs((PI-pi)/PI)*100)
    
print(pi)
plt.title(' Monte Carlo')
plt.xlabel('Iterative time(s)')
plt.ylabel('Absolute error')

plt.grid(linestyle='dotted', linewidth=1)
plt.plot(x_, yy)
plt.show()



