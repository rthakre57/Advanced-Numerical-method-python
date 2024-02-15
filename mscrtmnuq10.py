# Fit a curve of the form y=x/(a+bx)  to the following data (3, 7.148 ), (5,10.231), (8,13.509),  (12,16.434) Generalize the program with input of data set. 
# Least square method
# fit the curve of the form  y = x/a+bx to given n data points
import numpy as np

# Reading value of n
n = int(input("How many data points? "))

# Creating numpy array X & Y to store n data points
X = np.zeros(n)
Y = np.zeros(n)
# Reading data
print("Enter data:")
for i in range(n):
    X[i] = float(input("X["+str(i)+"]= "))
    Y[i] = float(input("Y["+str(i)+"]= "))

#find x and y
x = np.zeros(n)
y = np.zeros(n)
for i in range(n):
    x[i]=1/X[i]
    y[i]=1/Y[i]

    
# Finding required sum for least square methods
sumX,sumY,sumX2,sumXY = 0,0,0,0
for i in range(n):
    sumX = sumX + x[i]
    sumY = sumY + y[i]
    sumX2 = sumX2 + x[i]*x[i]
    sumXY = sumXY + (x[i]*y[i])

print(sumX,sumY,sumX2,sumXY)

# Finding coefficients A1 and A0 and Y
A1 = (n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
A0 = (sumY - A1*sumX)/n
print('Y=%0.8f + %0.8f X' %(A0,A1))

# Obtaining a and b and y 
a=A1
b=A0
print('a=',a)
print('b=',b)

print('The rquired fit is :y=x/%0.8f + %0.8f x' %(a, b))


# python output
How many data points? 4
Enter data:
X[0]= 3
Y[0]= 7.148
X[1]= 5
Y[1]= 10.231
X[2]= 8
Y[2]= 13.509
X[3]= 12
Y[3]= 16.434
0.7416666666666667 0.37251561141347045 0.17368055555555556 0.08050540081521017
Y=0.03450017 + 0.31619988 X
a= 0.3161998833702552
b= 0.03450017447846613
The rquired fit is :y=x/0.31619988 + 0.03450017 x
