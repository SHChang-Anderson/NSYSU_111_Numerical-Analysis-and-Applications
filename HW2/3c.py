import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm
# 生成一個標準常態分布的亂數

outyforvar = []

oux = []
ouy = []
xx = []
yy = []
# 設定初始 2D 向量



yy.clear
xx.clear

l = 200
theta = np.pi/4
vec = np.array([l*np.cos(theta), l*np.sin(theta)])
xyas = [1,0]
# 生成兩組隨機噪聲，並添加到實部和虛部
mu, sigma = 0, 1
noise_re = np.random.normal(mu, sigma, 20000)
noise_im = np.random.normal(mu, sigma, 20000)

for i in range(20000):
    noise_re[i] = vec[0] + noise_re[i]


for i in range(20000):
    noise_im[i] = vec[1] + noise_im[i]


for i in range (20000):
    angle1 = math.atan2(noise_re[i],noise_im[i])
    yy.append(angle1 * 180 /math.pi)
    xx.append(i+1)
    
mean = sum(yy) / len(yy)
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var)
ouy.append(mean)
oux.append(200)
outyforvar.append(st_dev)

print("mean" +str(mean))
print("dev" +str(st_dev))








l = 80
theta = np.pi/4
vec = np.array([l*np.cos(theta), l*np.sin(theta)])
xyas = [1,0]
# 生成兩組隨機噪聲，並添加到實部和虛部
mu, sigma = 0, 1
noise_re = np.random.normal(mu, sigma, 20000)
noise_im = np.random.normal(mu, sigma, 20000)


for i in range(20000):
    noise_re[i] = vec[0] + noise_re[i]


for i in range(20000):
    noise_im[i] = vec[1] + noise_im[i]


for i in range (20000):
    angle1 = math.atan2(noise_re[i],noise_im[i])
    yy.append(angle1 * 180 /math.pi)
    xx.append(i+1)

mean = sum(yy) / len(yy)
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var)
ouy.append(mean)
oux.append(80)
outyforvar.append(st_dev)
print("mean" +str(mean))
print("dev" +str(st_dev))


yy.clear
xx.clear

l = 40
theta = np.pi/4
vec = np.array([l*np.cos(theta), l*np.sin(theta)])
xyas = [1,0]
# 生成兩組隨機噪聲，並添加到實部和虛部
mu, sigma = 0, 1
noise_re = np.random.normal(mu, sigma, 20000)
noise_im = np.random.normal(mu, sigma, 20000)

for i in range(20000):
    noise_re[i] = vec[0] + noise_re[i]


for i in range(20000):
    noise_im[i] = vec[1] + noise_im[i]


for i in range (20000):
    angle1 = math.atan2(noise_re[i],noise_im[i])
    yy.append(angle1 * 180 /math.pi)
    xx.append(i+1)

mean = sum(yy) / len(yy)
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var)

ouy.append(mean)
oux.append(40)
outyforvar.append(st_dev)
print("mean" +str(mean))
print("dev" +str(st_dev))



yy.clear
xx.clear

l = 20
theta = np.pi/4
vec = np.array([l*np.cos(theta), l*np.sin(theta)])
xyas = [1,0]
# 生成兩組隨機噪聲，並添加到實部和虛部
mu, sigma = 0, 1
noise_re = np.random.normal(mu, sigma, 20000)
noise_im = np.random.normal(mu, sigma, 20000)

for i in range(20000):
    noise_re[i] = vec[0] + noise_re[i]


for i in range(20000):
    noise_im[i] = vec[1] + noise_im[i]


for i in range (20000):
    angle1 = math.atan2(noise_re[i],noise_im[i])
    yy.append(angle1 * 180 /math.pi)
    xx.append(i+1)
    #print(angle1 * 180 /math.pi)

mean = sum(yy) / len(yy)
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var)
ouy.append(mean)
oux.append(20)
outyforvar.append(st_dev)
print("mean" +str(mean))
print("dev" +str(st_dev))




yy.clear
xx.clear

l = 10
theta = np.pi/4
vec = np.array([l*np.cos(theta), l*np.sin(theta)])
xyas = [1,0]
# 生成兩組隨機噪聲，並添加到實部和虛部
mu, sigma = 0, 1
noise_re = np.random.normal(mu, sigma, 20000)
noise_im = np.random.normal(mu, sigma, 20000)

for i in range(20000):
    noise_re[i] = vec[0] + noise_re[i]


for i in range(20000):
    noise_im[i] = vec[1] + noise_im[i]


for i in range (20000):
    angle1 = math.atan2(noise_re[i],noise_im[i])
    yy.append(angle1 * 180 /math.pi)
    xx.append(i+1)

mean = sum(yy) / len(yy)
var = sum((i - mean)**2 for i in yy) / len(yy)
st_dev = math.sqrt(var)
ouy.append(mean)
oux.append(10)
outyforvar.append(st_dev)

print("mean" +str(mean))
print("dev" +str(st_dev))






#print(noise_im)
# 計算帶噪聲向量的相位角

# 繪製相位角分佈的直方圖


plt.plot(oux, ouy ,marker = "o", color='red')
plt.xlabel('length (r)')
plt.ylabel('Theta(°)')
plt.title('Mean at different lengths')
plt.show()



plt.plot(oux, outyforvar ,marker = "o", color='red')
plt.xlabel('length (r)')
plt.ylabel('Theta(°)')
plt.title('Standard deviation at different lengths')
plt.show()