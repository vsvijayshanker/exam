
import numpy as np
import matplotlib.pyplot as plt

def f(x,y1,y2):
    return np.array([32*y1+66*y2+2/3*x+2/3,-66*y1-133*y2-1/3*x-1/3])



a=0
b=0.5
h=0.01
n=int((b-a)/h+1)

y1=np.zeros(n)
y2=np.zeros(n)

x=np.linspace(a,b,n)

for i in range(n-1):
    dy=h*f(x[i],y1[i],y2[i])
    y1[i+1]=y1[i]+dy[0]
    y2[i+1]=y2[i]+dy[1]


ytest=(2*y1+y2)/x
print(y1,y1)

plt.subplots()
plt.plot(x,y1,label='y1',color='red')
plt.plot(x,y2,label='y2',color='green')
plt.plot(x,ytest,label='ytest',color='purple')

plt.legend()
plt.show()
