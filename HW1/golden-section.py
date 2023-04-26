from dis import code_info
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
        [0,math.cos(the*(math.pi/180)),-math.sin(the*(math.pi/180))],
        [0,math.sin(the*(math.pi/180)),math.cos(the*(math.pi/180))]
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


y_axis=[]
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
x1=0
x2=90
GR=(math.sqrt(5)-1)/2
print(GR)
print("Iter    Xl   Xu   Error")


while(1):
    d=GR*(x2-x1) 
    a=x1+d
    b=x2-d
    ini=np.array([
            [0],
            [0],
            [1]
    ])
    for j in range(500):
        res1=simulator(a,t,ini,T1,T2)
        if(j==499):
            break
        res1=cleanup(res1)
        ini=res1
    ini=np.array([
            [0],
            [0],
            [1]
    ])
    for j in range(500):
        res2=simulator(b,t,ini,T1,T2)
        if(j==499):
            break
        res2=cleanup(res2)
        ini=res2
    
    ans1=math.sqrt(res1[0][0]*res1[0][0]+res1[1][0]*res1[1][0])
    ans2=math.sqrt(res2[0][0]*res2[0][0]+res2[1][0]*res2[1][0])
    if(ans1<ans2):
        errorr=(1-GR)*abs((a-x1)/b)*100
        x2=a

    if(ans1>ans2):
        errorr=(1-GR)*abs((x2-b)/a)*100
        x1=b
    #
    x_axis.append(count)
    count=count+1

    y_axis.append(errorr)
    print("%2d,%2f,%2f,%2f" %(count-1,x1,x2,errorr))

    if(errorr<0.001):
        anss=(x1+x2)/2
        break

    


print(anss)
plt.title('Golden-Section Method')
plt.xlabel('Iteration(s)')
plt.ylabel('Error(%)')
plt.grid(linestyle='dotted', linewidth=1)
plt.plot(x_axis, y_axis,marker=".")
plt.show()
