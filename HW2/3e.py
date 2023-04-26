from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
from scipy.stats import norm
S0 = 100
T2 = 32
t1 = 10
t2 = 50
t3 = 90
X = [[1,10],[1,50],[1,90]]
rand_nums = np.random.normal(loc=0, scale=1, size=20000)
theta0 = 0
omega = math.pi / 200
yy = []
xx = []
annngle = [[0],[0],[0]]
Sum = 0
S = []
Sre = []
Sim = []
aa = [[0],[0]]

for z in range(3):
    S.append(0)
    Sre.append(0)
    Sim.append(0)



for z in range(20000):
    mu, sigma = 0, 1
    noise_re = np.random.normal(mu, sigma, 3)
    noise_im = np.random.normal(mu, sigma, 3)

# generate signal
    S[0] = S0* cmath.exp( -t1/T2 + (omega*t1 + theta0)*1j )
    S[1] = S0* cmath.exp( -t2/T2 + (omega*t2 + theta0)*1j )
    S[2] = S0* cmath.exp( -t2/T2 + (omega*t2 + theta0)*1j )

    Sre[0] = S[0].real
    Sim[0] = S[0].imag

    Sre[1] = S[1].real
    Sim[1] = S[1].imag

    Sre[2] = S[2].real
    Sim[2] = S[2].imag

# add noise
    for i in range(3):
        noise_re[i] = Sre[i] + noise_re[i]


    for i in range(3):
        noise_im[i] = Sim[i] + noise_im[i]

    for i in range(3):
        angle1 = math.atan2(noise_re[i],noise_im[i])
        annngle[i][0] = (angle1 * 180 /math.pi)


# regression
    Xt = np.transpose(X)
    temper = np.linalg.inv(Xt.dot(X)).dot(Xt).dot(annngle)
    yy.append(temper[1][0])


mean = sum(yy) / len(yy)
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var)

print("mean: " +str(mean))
print("dev: " +str(st_dev))

plt.hist(yy, bins=50, density=True, alpha=0.7, color='blue',edgecolor =  "black")
plt.xlabel('ω')
plt.ylabel('Frequency')
plt.title('Distribution of ω after 20000 regressions')
plt.show()




x_vals = np.linspace(-0.6 , -0.3)


y_vals = norm.pdf(x_vals, loc=mean, scale=st_dev)


plt.hist(yy, bins=50, density=True, alpha=0.7, color='blue',edgecolor =  "black")
plt.plot(x_vals, y_vals, color='red')
plt.xlabel('ω')
plt.ylabel('Frequency')
plt.title('Distribution of ω after 20000 regressions')
plt.show()