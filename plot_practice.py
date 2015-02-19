import numpy as np
import matplotlib.pyplot as plt
import pdb

OSC_FREQ =  1.1;
SAMPLE_RATE = 1
N = 8
fs = 8000.0
ts = 1.0 / fs
DURATION = N * ts
m = 1

def f(t):
	#return np.sin(2*np.pi*t*1000) + 0.5 * np.sin(2*np.pi*t*2000 + 3*np.pi / 4)
	return np.sin(2*np.pi*t*10) 
	
def ftSin(t):
	return np.sin(2*np.pi*t * m * (1 / DURATION) )
	
	
def ftCos(t):
	return np.cos(2*np.pi*t * m * (1 / DURATION) )
	
	
t1 = np.arange(0.0, DURATION, float(DURATION) / 1000.0)

t2 = np.arange(0.0, DURATION , ts)

plt.plot(t1, f(t1) )
plt.plot(t2, f(t2) , "ro")

#sin illustration
plt.plot( t1,  ftSin(t1) , "g--")

#sin samples
sinComponent = ftSin(t2) * f(t2)
plt.plot(t2, sinComponent , "go")

plt.plot(t2, [sinComponent.sum() for x in t2] , "g")

#cos illustration
plt.plot( t1,  ftCos(t1) , "g--")

cosComponent = ftCos(t2) * f(t2)

plt.show()