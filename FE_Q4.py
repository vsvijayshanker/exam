
import numpy as np
import matplotlib.pyplot as plt

x=np.random.random(1024)

print('max is',max(x),'\n','min is',min(x))
print(x)

plt.subplots()
plt.plot(x)
plt.subplots()
plt.plot(x,'o',color='green')
plt.subplots()
plt.hist(x)

plt.legend()
plt.show()

