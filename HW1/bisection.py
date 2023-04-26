import matplotlib.pyplot as plt
import numpy as np
import math
#my_text=sg.Text('Bisection')
#showFigure=sg.Button('Show Figure')
#ExitBotton=sg.Button('Exit')
#layout = [
#    [showFigure,ExitBotton]
    
#]
#window = sg.Window('Bisection',layout)
#while True:
#    event, value = window.read()
#window.close()

x_axis=[]   #for iterative times
y_axis=[]   #for Relative error
x1=0  #initial left node
x2=0.5 #initial right node
oldx=0  #initialize root
count=1 #count iterative times
print('       Xl          Xu          Xr          Error' )
while(1):
    newx=(x1+x2)/2
    newroot = ((10*math.cos(3*newx * math.pi / 2)) * math.exp(-newx)) + newx**6-1   #compute newroot's value

    lroot = ((10*math.cos(3*x1 * math.pi / 2)) * math.exp(-x1)) + x1**6-1
    
    rroot = ((10*math.cos(3*x2 * math.pi / 2)) * math.exp(-x2)) + x2**6-1
    
    lfloor=newroot*lroot    #check if same sign
    
    rseiling=newroot*rroot  #check if same sign
    
    if(lfloor>0):
        x1=newx
    elif(rseiling>0):
        x2=newx

    errorr=abs(((newx-oldx)/newx)*100)
    
    print('%2d.   %2f  %2f   %2f   %2f' % (count,x1,x2,newx,errorr))
    if(abs(errorr)<0.01):   #Termination condition
        break
    oldx=newx
    x_axis.append(count)
    y_axis.append(errorr)
    count=count+1
print(newx)
plt.grid()
plt.title('Bisection')
plt.xlabel('Iterative Time(s)')
plt.ylabel('Relative Error(%)')
plt.plot(x_axis, y_axis,marker="o")
plt.show()


        