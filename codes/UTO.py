#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt

x = np.linspace(-4,4,30)#points on the x axis
y1 = np.zeros(30)
y2 = 1 - np.exp(-x/2)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar=np.random.uniform(size=10**6)
randvar = -2*np.log(1 - randvar)
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')
plt.savefig('/home/ravisha/Documents/EE5600/Assignment_3/UTO_cdf.pdf')
plt.savefig('/home/ravisha/Documents/EE5600/Assignment_3/UTO_cdf.eps')

