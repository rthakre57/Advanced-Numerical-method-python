Q 15 . Determine the value of when , given that ( ) and by Modified Euler’s method.
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
    y=np.zeros((n))
    x=np.zeros((n))
    for k in range(1):
        x[k]=x0
    for l in range(1,n):
        x[l]=x[l-1]+h
        print('__________________________')
        print('Step'+str(l)+':')
        # By Euler Method
        y[0]=y0
        y[1]=y0+h*f(x0,y0)
        print('By Eulers method y=',y[0])
        for j in range(2,n):         
            # By Modified Euler Method
            y[j]=y[j-2]+h/2*(f(x[j-2],y[j-2])+f(x0+h,y[j-1]))
            #if (round(y[j-1],2)==round(y[j],2)):
            print('By Modified Eulers method y=',y[j])
            print('\nAt x=%.4f, y=%.4f' %(x[l],y[j]))
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
m=((xn-x0)/h)+1
print('Number of steps=',m)
n = int(input('Number of steps = '))

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
Number of steps= 3.0
Number of steps = 3
__________________________
Step1:
By Eulers method y= 1.0
By Modified Eulers method y= 1.0513125

At x=0.0500, y=1.0513
__________________________
__________________________
Step2:
By Eulers method y= 1.0
By Modified Eulers method y= 1.0513125

At x=0.1000, y=1.0513
__________________________
