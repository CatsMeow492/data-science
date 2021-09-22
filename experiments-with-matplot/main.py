import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000) #id array of length 1000 from 0 to 10

y = np.sin(x)
plt.plot(x,np.sin(x), 'k:', label='sin(x)')
plt.plot(x,np.cos(x), 'r--',label='cos(x)')
plt.legend()
plt.savefig('plot.png')
plt.show()

