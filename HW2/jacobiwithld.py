import matplotlib.pyplot as plt
import numpy as np
import math

lambdaa = 0.3 # relaxation with λ = [0.3,0.7,1.2]

oldx=np.array([[1],[1],[1],[1],[1],[1]])
matrixxD = np.array([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,30,0],[0,0,0,0,0,-25]])
matrixxDht = np.array([[0,-1,0,0,0,-1],[0,0,-1,0,0,0],[0,0,0,-1,0,0],[0,0,0,0,-1,1],[8,0,0,0,0,25],[0,12,5,15,0,0]])
matrixx = np.array([[1,-1,0,0,0,-1],[0,1,-1,0,0,0],[0,0,1,-1,0,0],[0,0,0,1,-1,1],[8,0,0,0,30,25],[0,12,5,15,0,-25]])
matrixxDiag=np.diagonal(matrixx)
matrixxinv = np.linalg.inv(matrixx)
b = [[0],[0],[0],[0],[100],[0]]

xr = matrixxinv.dot(b)

matrixxnv = np.linalg.inv(matrixxD)

err1=[]
err2=[]
err3=[]
err4=[]
err5=[]
err6=[]
xyais=[]
output=[]
outer=[]


j = 1
while(1):
    temper=matrixxDht.dot(oldx)
    temper=b-temper
    newx = matrixxnv.dot(temper)
    newx = lambdaa * newx + (1 - lambdaa) * oldx 
 

    err1.append(abs((newx[0][0]-xr[0])/xr[0])*100)
    err2.append(abs((newx[1][0]-xr[1])/xr[1])*100)
    err3.append(abs((newx[2][0]-xr[2])/xr[2])*100)
    err4.append(abs((newx[3][0]-xr[3])/xr[3])*100)
    err5.append(abs((newx[4][0]-xr[4])/xr[4])*100)
    err6.append(abs((newx[5][0]-xr[5])/xr[5])*100)

    nowerr1 = (abs((newx[0][0]-xr[0])/xr[0])*100)
    nowerr2 = (abs((newx[1][0]-xr[1])/xr[1])*100)
    nowerr3 = (abs((newx[2][0]-xr[2])/xr[2])*100)
    nowerr4 = (abs((newx[3][0]-xr[3])/xr[3])*100)
    nowerr5 = (abs((newx[4][0]-xr[4])/xr[4])*100)
    nowerr6 = (abs((newx[5][0]-xr[5])/xr[5])*100)

    
    xyais.append(j)

    j = j + 1
    oldx=newx

    if(nowerr1 < 0.1 and nowerr2 < 0.1 and nowerr3 < 0.1 and nowerr4 < 0.1 and nowerr5 < 0.1 and nowerr6 < 0.1):
        print("Iterative time(s): " + str(j-1))
        break

    if(j - 1 > 500):
        break


plt.title('Jacobi method relaxation with λ = [0.3]')
plt.xlabel('Iterative time(s)')
plt.ylabel('Absolute error')

plt.grid(linestyle='dotted', linewidth=1)
plt.plot(xyais, err1)
plt.plot(xyais, err2)
plt.plot(xyais, err3)



plt.plot(xyais, err4)
plt.plot(xyais, err5)
plt.plot(xyais, err6)

plt.legend(['I12','I23','I34','I45','I56','I25'])
plt.show()





