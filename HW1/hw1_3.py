import matplotlib.pyplot as plt
import numpy as np
import math

x=0
y=0
z=1
count=1
def Rotate(the,S_minus):
    rt=np.array([
        [1,0,0],
        [0,math.cos(math.radians(the)),-(math.sin(math.radians(the)))],
        [0,math.sin(math.radians(the)),math.cos(math.radians(the))]
    ])

    S_plus=rt.dot(S_minus)
    
    return S_plus

def magnitude_modul(S_minus,t,T1,T2):
    D1=np.array([
        [math.exp(-t/T2),0,0],
        [0,math.exp(-t/T2),0],
        [0,0,math.exp(-t/T1)]
    ])
    D2=np.array([
        [0],
        [0],
        [1-math.exp(-t/T1)]
    ])
    S_plus=D1.dot(S_minus)+D2
 
    return S_plus

def cleanup(S_minus):
    cl=np.array([
        [0,0,0],
        [0,0,0],
        [0,0,1]
    ])
    
    S_plus=cl.dot(S_minus)
    return S_plus


def simulator(the,t,S_minus,T1,T2):
    temp=Rotate(the,S_minus)
    S_plus=magnitude_modul(temp,t,T1,T2)
    
    return S_plus


Sxy=[]
x_axis=[]
ini=np.array([
        [0],
        [0],
        [1]
    ])
t=250
T1=1500
T2=200
maxy=0
maxx=0
for i in np.arange(0,90,0.5):
    ini=np.array([
        [0],
        [0],
        [1]
    ])
    for j in range(500):
        res=simulator(i,t,ini,T1,T2)
        if(j==499):
            break
        res=cleanup(res)
        ini=res

    Sxy.append(math.sqrt(res[0][0]*res[0][0]+res[1][0]*res[1][0]))
    x_axis.append(i)
    if((math.sqrt(res[0][0]**2+res[1][0]**2))>maxy):
        maxy=math.sqrt(res[0][0]**2+res[1][0]**2)
        maxx=i


plt.title('figure')
plt.xlabel('Theta')
plt.ylabel('Sxy')
plt.scatter([maxx],[maxy],c='r')
plt.text(maxx, maxy, 'max' , ha='center', va='bottom', fontsize=10.5)
plt.grid(linestyle='dotted', linewidth=1)
plt.plot(x_axis, Sxy,marker=".")
plt.show()
