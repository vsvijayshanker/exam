
import numpy as np
import matplotlib.pyplot as plt

n=1024
x=np.random.random(n)

freqs=fft.freq(n)

mask=freqs>0

fft_vals=fft(x)

fft_theo=2.0*(np.abs(fft_val/n)**2)

print('max is',max(x),'\n','min is',min(x))
print(x)

plt.subplots()
plt.plot(x)
plt.subplots()
plt.plot(x,'o',color='green')
plt.subplots()
plt.hist(x)

plt.plot(fft_theo)
plt.legend()
plt.show()

