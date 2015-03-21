import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0,1.001,0.001)
y = [math.e**(-5*value) for value in x]
line1,=plt.plot(x, y, label='Object Function')

h = 0.05
T = np.arange(0,1.05,h)
U = np.zeros(21)
U[0]=1
for i in range(1,20):
    U[i] = (1-5*h)*U[i-1]
line2,=plt.plot(T, U, label='Euler')

V=np.zeros(21)
V[0]=1
for i in range(1,20):
    W=np.zeros(1000)
    W[0]=V[i-1]
    k=1
    while k>0:
        W[k]=V[i-1]-5*h/2*(V[i-1]+W[k-1])
        if abs(W[k]-W[k-1])<1e-4:
            break
        k=k+1
    V[i]=W[k]
line3,=plt.plot(T, V, label='Upgrad Euler')

plt.legend(handles=[line1,line2,line3],loc=1)
plt.title('Euler Method')
plt.xlabel('t')
plt.ylabel('u')
plt.show()
