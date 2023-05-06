import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math
from scipy import integrate
# function 1
def f1(x):
    return 0.2 + 25*x - 200*(x**2) + 675*(x**3)

a = 0
b = 0.8
# Actual solution 
trueans, err = integrate.quad(f1,a,b)
#print(trueans)


# Two Point Gauss Quadrature Rule
c1 = (b-a) / 2
c2 = (b-a) / 2
x1 = (b-a)/2 * (-1 / math.sqrt(3)) + (b+a) /2
x2 = (b-a)/2 * (1 / math.sqrt(3)) + (b+a) /2
guessans = c1 * f1(x1) + c2 * f1(x2)
#print(guessans)

print(abs((guessans - trueans) / trueans ))





# function 2

y = []
x = []

def f2(x,a1):
    return 0.2 + 25*x - 200*(x**2) + 675*(x**3) - a1*(x**4)

for i in range(0,100):

    a = 0
    b = 0.8

    # Actual solution 
    trueans, err = integrate.quad(f2,a,b,args=(i))


    # Two Point Gauss Quadrature Rule
    c1 = (b-a) / 2
    c2 = (b-a) / 2
    x1 = (b-a)/2 * (-1 / math.sqrt(3)) + (b+a) /2
    x2 = (b-a)/2 * (1 / math.sqrt(3)) + (b+a) /2
    guessans = c1 * f2(x1,i) + c2 * f2(x2,i)



    y.append(abs((guessans - trueans) / trueans )*100)
    x.append(i)



# x_vals = np.linspace(-4, 4, 1000)


# y_vals = norm.pdf(x_vals, loc=0, scale=1)



plt.plot(x, y, color='red')
plt.xlabel('X to the power of 4 coefficient')
plt.ylabel('relative error (%)')
plt.title('Two Point Gauss Quadrature Rule')
plt.show()

