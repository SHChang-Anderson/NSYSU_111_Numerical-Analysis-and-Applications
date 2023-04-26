import matplotlib.pyplot as plt
import numpy as np
import math

lambdaa = 1.2 # relaxation with λ = [0.3,0.7,1.2]


matrixxD = np.array([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,30,0],[0,0,0,0,0,-25]])
matrixxDht = np.array([[0,-1,0,0,0,-1],[0,0,-1,0,0,0],[0,0,0,-1,0,0],[0,0,0,0,-1,1],[8,0,0,0,0,25],[0,12,5,15,0,0]])
matrixx = np.array([[1,-1,0,0,0,-1],[0,1,-1,0,0,0],[0,0,1,-1,0,0],[0,0,0,1,-1,1],[8,0,0,0,30,25],[0,12,5,15,0,-25]])
matrixxDiag=np.diagonal(matrixx)
matrixxinv = np.linalg.inv(matrixx)
b = [[0],[0],[0],[0],[100],[0]]

xr = matrixxinv.dot(b)



init = []

temp = []

err1=[]
err2=[]
err3=[]
err4=[]
err5=[]
err6=[]


xayes = []

for i in range (6):
    init.append(1)

old = []

for i in range (6):
    old.append(init[i])

ans = []
for i in range (6):
    ans.append(init[i])


count = 0


while(1):
    count = count + 1
    ans[0] = old[1] + old[5]
    ans[0] = lambdaa*ans[0] + (1-lambdaa) * old[0]
    
    ans[1] = old[2]
    ans[1] = lambdaa*ans[1] + (1-lambdaa) * old[1]

    ans[2] = old[3]
    ans[2] = lambdaa*ans[2] + (1-lambdaa) * old[2]

    ans[3] = old[4] - old[5]
    ans[3] = lambdaa*ans[3] + (1-lambdaa) * old[3]

    ans[4] = ( 100 - 8 * ans[0] - 25 * old[5] ) / 30
    ans[4] = lambdaa*ans[4] + (1-lambdaa) * old[4]

    ans[5] = ( 12*ans[1] + 5*ans[2] + 15*ans[3] ) / 25
    ans[5] = lambdaa*ans[5] + (1-lambdaa) * old[5]


    err1.append(abs((ans[0]-xr[0][0])/xr[0][0])*100)
    err2.append(abs((ans[1]-xr[1][0])/xr[1][0])*100)
    err3.append(abs((ans[2]-xr[2][0])/xr[2][0])*100)
    err4.append(abs((ans[3]-xr[3][0])/xr[3][0])*100)
    err5.append(abs((ans[4]-xr[4][0])/xr[4][0])*100)
    err6.append(abs((ans[5]-xr[5][0])/xr[5][0])*100)



    nowerr1 = (abs((ans[0]-xr[0])/xr[0][0])*100)
    nowerr2 = (abs((ans[1]-xr[1])/xr[1][0])*100)
    nowerr3 = (abs((ans[2]-xr[2])/xr[2][0])*100)
    nowerr4 = (abs((ans[3]-xr[3])/xr[3][0])*100)
    nowerr5 = (abs((ans[4]-xr[4])/xr[4][0])*100)
    nowerr6 = (abs((ans[5]-xr[5])/xr[5][0])*100)

    for j in range(6):
        old[j] = ans[j]


    xayes.append(count)


    if(nowerr1 < 0.1 and nowerr2 < 0.1 and nowerr3 < 0.1 and nowerr4 < 0.1 and nowerr5 < 0.1 and nowerr6 < 0.1):
        print("Iterative time(s): " + str(count))
        break

    if(count > 100):
        break







plt.title('Gauss-Seidel method with λ = [0.3]')
plt.xlabel('Iterative time(s)')
plt.ylabel('Absolute error')

plt.grid(linestyle='dotted', linewidth=1)
plt.plot(xayes, err1)
plt.plot(xayes, err2)
plt.plot(xayes, err3)



plt.plot(xayes, err4)
plt.plot(xayes, err5)
plt.plot(xayes, err6)

plt.legend(['I12','I23','I34','I45','I56','I25'])
plt.show()




