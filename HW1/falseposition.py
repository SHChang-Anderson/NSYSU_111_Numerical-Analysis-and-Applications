import matplotlib.pyplot as plt
import numpy as np
import math
x_axis=[]
y_axis=[]
x1=0 #setting Boundary conditions
x2=0.5  #setting Boundary conditions
oldx=0
count=1
print('       Xl          Xu          Xr          Error' )
while(1):
    y1=((10*math.cos(3*x1 * math.pi / 2)) * math.exp(-x1)) + x1**6-1
    y2=((10*math.cos(3*x2 * math.pi / 2)) * math.exp(-x2)) + x2**6-1
    slope=(y2-y1)/(x2-x1)
    if(slope>0):
        b=y1-slope*x1
        newx=(-b)/slope
        errorr=abs(((newx-oldx)/newx)*100)
        x1=newx
    elif(slope<0):
        b=y1-slope*x1
        newx=(-b)/slope
        errorr=abs(((newx-oldx)/newx)*100)
        x2=newx
    print('%2d.   %2f  %2f   %2f   %2f' % (count,x1,x2,newx,errorr))
    oldx=newx
    x_axis.append(count)
    y_axis.append(errorr)
    count=count+1
    if(abs(errorr)<0.01):   #Termination condition
        break
print(newx)
plt.title('FalsePositoin')
plt.grid()
plt.xlabel('Iterative Time(s)')
plt.ylabel('Relative Error(%)')
plt.plot(x_axis, y_axis,marker="o")
plt.show()