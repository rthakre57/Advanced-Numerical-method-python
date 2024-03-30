# Modified Euler method python program
import numpy as np
# function to be solved
def f(x,y):
    return x**2 +y

# or
# f = lambda x: x+y

# Euler method
def Modified_euler(x0,y0,xn,h):
    
    # Calculating step size
    #h = (xn-x0) 
    y=np.zeros((n+1))
    x=np.zeros((n+1))
    z=np.zeros((n+1))
    x[0]=x0
    y[0]=y0
    for l in range(1,n):
        x[l]=x[l-1]+h
        print('__________________________')
        print('Step'+str(l)+':')
        # By Euler Method
        for i in range(1,n):
            y[i]=y[i-1]+h*f(x[i-1],y[i-1])
            #y[1]=y0+h*f(x0,y0)
            print('By Eulers method y=',y[i])     
            # By Modified Euler Method
            for j in range(1,n+1):
                z[j]=y[i-1]+h/2*(f(x[i-1],y[i-1])+f(x[i],y[i]))
                y[i]=z[j]

            #if (round(y[j-1],2)==round(y[j],2)):
            print('By Modified Eulers method y=',y[i])
            print('\nAt x=%.4f, y=%.4f' %(x[l],z[i]))
            print('__________________________')
    
                
# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))  


print('Enter calculation point: ')
xn = float(input('xn = '))
#step size
h=float(input('Step size h='))

print('Enter number of steps:')
m=int(((xn-x0)/h)+1)
#print('Number of steps=',m)
#n = int(input('Number of steps = '))
n=m
# Modified Euler method call

Modified_euler(x0,y0,xn,h)

Python Output:
Enter initial conditions:
x0 = 0
y0 = 1
Enter calculation point:
xn = 0.1
Step size h=0.05
Enter number of steps:
__________________________
Step1:
By Eulers method y= 1.05
By Modified Eulers method y= 1.0513461328125

At x=0.0500, y=1.0513
__________________________
By Eulers method y= 1.104038439453125
By Modified Eulers method y= 1.1053254015655822

At x=0.0500, y=1.1053
__________________________
__________________________
Step2:
By Eulers method y= 1.05
By Modified Eulers method y= 1.0513461328125

At x=0.1000, y=1.0513
__________________________
By Eulers method y= 1.104038439453125
By Modified Eulers method y= 1.1055818078155824

At x=0.1000, y=1.1056
__________________________
