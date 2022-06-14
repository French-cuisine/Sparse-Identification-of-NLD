import numpy as np
import matplotlib.pyplot as plt

"""this is an 1-dimensional Ordinary Differential Equation Initial Value Problem solver. It uses RK4 method """


def ode4(events ,init_val, x, relTol = None, absTol = None):
    y = np.zeros(len(x))
    y[0] = init_val
     
    h = x[1]-x[0]

    if relTol == None :
        relTol = 0
    
    if absTol == None :
        absTol = 0


    for i in range(1,len(x)):
        k1 = h*events(x[i-1],y[i-1])
        k2 = h*events(x[i-1]+h/2,y[i-1]+k1/2)
        k3 = h*events(x[i-1]+h/2,y[i-1]+k2/2)
        k4 = h*events(x[i-1]+h,y[i-1]+k3)

        k = (k1+2*k2+2*k3+k4)/6

        y[i] = y[i-1] + k 


    return y

 

"""def f(x, y):
    dydt = -y 
    return dydt

t = np.linspace(0 ,10 , 1000)

y = ode4(f ,1 ,t)


z = np.exp(-t)
plt.plot(t,y, color="r", label = "Numerical solved function")
plt.plot(t,z, color="g", label = "Analytical solved function")
#plt.plot(t,k, color="b", label = "Analytical solved function")
plt.legend()

plt.show()"""