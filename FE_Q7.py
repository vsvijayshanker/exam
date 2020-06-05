#pseudo randomnumber generator

import numpy as np

m=5
a=818
c=928

n=20
x=np.zeros(n)
for i in range(n-1):
    x[0]=2
    x[i+1]=(a*x[i]+c)%m

print('\nfor seed=2 which appears in psudorandom sequence\n',x)

for i in range(n-1):
    x[0]=7
    x[i+1]=(a*x[i]+c)%m

print('\nfor seed=7 which never appears in psudorandom sequence\n',x)
