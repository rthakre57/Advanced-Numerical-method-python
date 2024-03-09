Q.16
# RK-4 method python program
import numpy as np
# function to be solved
def f(x,y):
    return y-x

# or
# f = lambda x: x+y

# RK-4 method
def rk4(x0,y0,xn,h):
    
    # Calculating step size
    #h = (xn-x0)/n
    y=np.zeros((n))
    x=np.zeros((n))
    for k in range(1):
        x[k]=x0
    for l in range(1,n):
        x[l]=x[l-1]+h
        y[0]=y0
        for i in range(l,l+1):
            print('\n--------SOLUTION--------')
            print('-------------------------')    
            print('x'+str(i)+'\ty'+str(i)+'')
            print('-------------------------')
            k1 = h * (f(x[i-1], y[i-1]))
            k2 = h * (f((x[i-1]+h/2), (y[i-1]+k1/2)))
            k3 = h * (f((x[i-1]+h/2), (y[i-1]+k2/2)))
            k4 = h * (f((x[i-1]+h), (y[i-1]+k3)))
            k = (k1+2*k2+2*k3+k4)/6
            y[i] = y[i-1] + k
            print('%.4f\t%.4f\t'% (x[l],y[i]))
            print('-------------------------')
            print('\nAt x=%.4f, y=%.4f' %(x[l],y[i]))
    print('\nAns:y(%0.5f)=(%0.5f)' %(x[l],y[i]))
# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

h = float(input('Enter the step size = '))

print('Enter number of steps:')
m=((xn-x0)/h)+1
print('Number of steps=',m)
n = int(input('Number of steps = '))

# RK4 method call
rk4(x0,y0,xn,h)

Python Output:
Enter initial conditions:
x0 = 0
y0 = 2
Enter calculation point:
xn = 0.1
Enter the step size = 0.05
Enter number of steps:
Number of steps= 3.0
Number of steps = 3

--------SOLUTION--------
-------------------------
x1      y1
-------------------------
0.0500  2.1013
-------------------------

At x=0.0500, y=2.1013

--------SOLUTION--------
-------------------------
x2      y2
-------------------------
0.1000  2.2052
-------------------------

At x=0.1000, y=2.2052

Ans:y(0.10000)=(2.20517)


Enter initial conditions:
x0 = 0
y0 = 2
Enter calculation point:
xn = 0.2
Enter the step size = 0.1
Enter number of steps:
Number of steps= 3.0
Number of steps = 3

--------SOLUTION--------
-------------------------
x1      y1
-------------------------
0.1000  2.2052
-------------------------

At x=0.1000, y=2.2052

--------SOLUTION--------
-------------------------
x2      y2
-------------------------
0.2000  2.4214
-------------------------

At x=0.2000, y=2.4214

Ans:y(0.20000)=(2.42140)
