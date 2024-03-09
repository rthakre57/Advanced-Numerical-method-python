Q 19 19. Solve numerically the equation with initial condition ( ) by Milne’s method from to (
import numpy as np

# Define the ODE function
def g(x, y):
    return x+y

def milnes_method(x0, y0, xn, h):
    y=np.zeros((n))
    x=np.zeros((n))
    f=np.zeros((n))
    for k in range(1):
        x[k]=x0
    for l in range(1,n):
        x[l]=x[l-1]+h
        y[0]=y0
        f[0]=g(x0,y0)
        for i in range(l,4):
            print('\n--------SOLUTION--------')
            print('-------------------------')    
            print('x'+str(i)+'\ty'+str(i)+'')
            print('-------------------------')
            k1 = h * (g(x[i-1], y[i-1]))
            k2 = h * (g((x[i-1]+h/2), (y[i-1]+k1/2)))
            k3 = h * (g((x[i-1]+h/2), (y[i-1]+k2/2)))
            k4 = h * (g((x[i-1]+h), (y[i-1]+k3)))
            k = (k1+2*k2+2*k3+k4)/6
            y[i] = y[i-1] + k
            print('%.4f\t%.4f\t'% (x[l],y[i]) )
            print('-------------------------')
            print('\nAt x=%.4f, y=%.4f' %(x[l],y[i]))
            f[i]=g(x[l],y[i])
            print('f'+str(i)+'=',f[i])
            
    for i in range(4,n):
        y[i]=y[i-4]+4*h/3*(2*f[i-3]+f[i-2]+2*f[i-1])
        print('By Milnes Predictor method')
        print('\nAt x=%.4f, y=%.4f' %(x[i],y[i]))
        f[i]=g(x[i],y[i])
        y[i]=y[i-2]+h/3*(f[i-2]+4*f[i-1]+f[i])
        print('By Milnes Corrector method')
        print('\nAt x=%.4f, y=%.4f' %(x[i],y[i]))



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

# Milnes method call
milnes_method(x0,y0,xn,h)


Python Output:
Enter initial conditions:
x0 = 1
y0 = 2
Enter calculation point:
xn = 1.4
Enter the step size = 0.1
Enter number of steps:
Number of steps= 4.999999999999999
Number of steps = 5

--------SOLUTION--------
-------------------------
x1      y1
-------------------------
1.1000  2.3207
-------------------------

At x=1.1000, y=2.3207
f1= 3.4206833333333333

--------SOLUTION--------
-------------------------
x2      y2
-------------------------
1.1000  2.6856
-------------------------

At x=1.1000, y=2.6856
f2= 3.785610283402778

--------SOLUTION--------
-------------------------
x3      y3
-------------------------
1.1000  2.9732
-------------------------

At x=1.1000, y=2.9732
f3= 4.0732289882501505

--------SOLUTION--------
-------------------------
x2      y2
-------------------------
1.2000  2.6856
-------------------------

At x=1.2000, y=2.6856
f2= 3.885610283402778

--------SOLUTION--------
-------------------------
x3      y3
-------------------------
1.2000  3.0994
-------------------------

At x=1.2000, y=3.0994
f3= 4.299433988250151

--------SOLUTION--------
-------------------------
x3      y3
-------------------------
1.3000  3.0994
-------------------------

At x=1.3000, y=3.0994
f3= 4.399433988250151
By Milnes Predictor method

At x=1.4000, y=4.6034
By Milnes Corrector method

At x=1.4000, y=3.6018
