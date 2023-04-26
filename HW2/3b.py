import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm


xx = []
yy = []
l = 200
theta = np.pi/4
vec = np.array([l*np.cos(theta), l*np.sin(theta)])
xyas = [1,0]

mu, sigma = 0, 1
noise_re = np.random.normal(mu, sigma, 20000)
noise_im = np.random.normal(mu, sigma, 20000)



for i in range(20000): # add noise 
    noise_re[i] = vec[0] + noise_re[i]


for i in range(20000): # add noise 
    noise_im[i] = vec[1] + noise_im[i]

angle = []
theta_noisy = []
for i in range (20000):
    angle1 = math.atan2(noise_re[i],noise_im[i])
    yy.append(angle1 * 180 /math.pi) #compute angle
    xx.append(i+1)
    

mean = sum(yy) / len(yy) # compute mean
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var) # compute mean Standard Deviation

print("mean: " +str(mean))
print("dev: " +str(st_dev))






plt.figure()

plt.hist(yy, bins=50, density=True, alpha=0.7, color='blue',edgecolor =  "black")

plt.xlabel('Theta(°)')
plt.ylabel('Frequency')
plt.title('Theta distribution')
plt.show()



x_vals = np.linspace(44,46 , 20000)

y_vals = norm.pdf(x_vals, loc=mean, scale=st_dev)

plt.hist(yy, bins=50, density=True, alpha=0.7, color='blue',edgecolor =  "black")
plt.plot(x_vals, y_vals, color='red')
plt.xlabel('Theta(°)')
plt.ylabel('Frequency')
plt.title('Theta distribution with Normal distribution')
plt.show()