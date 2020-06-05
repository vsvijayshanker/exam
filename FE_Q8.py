import numpy as np
import matplotlib.pyplot as plt

h=0.1
a=0
b=1
n=int(1+(b-a)/h)

x=np.linspace(a,b,n)
y=np.zeros(n)
ytr=np.zeros(n)
y1=np.zeros(n)
y2=np.zeros(n)
ya=0
yb=2

def ftrue(x):
    return np.exp(2)/(np.exp(4)-1)*(np.exp(2*x)-np.exp(-2*x))+x

def f(x,y,y1):
    return np.array([y1,4*(y-x)])

for i in range(n):
    ytr[i]=ftrue(x[i])


for j in range(8):
    y1[0]=1+j*0.2
    y[0]=a
    for i in range(n-1):
        df=h*f(x[i],y[i],y1[i])
        y1[i+1]=y1[i]+df[1]
        y[i+1]=y[i]+df[0]
    plt.plot(x,y,'--')


plt.plot(x,ytr,'--',marker='o',label='original function')

plt.minorticks_on()
plt.grid()
plt.grid(which='minor',linewidth='0.1')
plt.grid(which='major',linewidth='1')
plt.legend()
plt.show()
