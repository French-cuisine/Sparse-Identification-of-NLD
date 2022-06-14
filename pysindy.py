import numpy as np
import matplotlib.pyplot as plt

def numdiff(x,step_size):
    
    xdot = [0]*len(x); 
    xdot[0] = (x[1]-x[0])/step_size 

    for i in range (1, len(x)-1):
        xdot[i] = (x[i+1] - x[i-1])/(2*step_size)
    
    xdot[len(x)-1] = (x[len(x)-1]-x[len(x)-2])/step_size
    
    return xdot 

#data for plotting

in_val = np.linspace(-np.pi/3,np.pi/3, 1000)
#print(in_val)
out_val = np.tan(in_val)
#print (out_val)
#print(type(out_val))
dt = in_val[1]-in_val[0]

out_valDot = numdiff(out_val, dt) 


plt.plot(in_val, out_val, color = 'r', label = 'sine')
plt.plot(in_val, out_valDot, color ='g', label = 'Derivative of sine')

plt.legend()

plt.show()