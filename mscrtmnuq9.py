#Find the cubic polynomial which takes the values: y(1 )=24,  y(3)=120,  y(5)=336,  y(7)=720 , and hence in particular find y(8) by Newton’s interpolation formula. 
import numpy as np
import math
# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n,n))


# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))

h=x[1]-x[0]
print(h)
# Generating forward difference table
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

        
print('\nFORWARD DIFFERENCE TABLE\n');

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()


print('\nNEWTON FORWARD DIFFERENCE INTERPOLATION FORMULA\n')

# Reading interpolation point
xp = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero

p = (xp-x[0])/h
print(p)

# Implementing Newtons Interpolation
yp = 0
z=1
zp=0
for i in range(1,n):
    #yp+=math.comb(p,i)*y[0][i]
    for j in range(i-1,i):
        z=z*((p-float(j))/(j+1))
        #print(z)
    zp+=z*y[0][i]
    #print(zp)    
    
yp=y[0][0]+zp
    
# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))


# Python Output:
Enter number of data points: 4
Enter data for x and y:
x[0]=1
y[0]=24
x[1]=3
y[1]=120
x[2]=5
y[2]=336
x[3]=7
y[3]=720
2.0

FORWARD DIFFERENCE TABLE

1.00            24.00           96.00           120.00          48.00
3.00            120.00          216.00          168.00
5.00            336.00          384.00
7.00            720.00

NEWTON FORWARD DIFFERENCE INTERPOLATION FORMULA

Enter interpolation point: 8
3.5
Interpolated value at 8.000 is 990.000.
y(8)=990.00000
