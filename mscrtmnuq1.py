#(RTMNU Practical Problem 1)  Find a real root of the equation 2x=〖log〗_10 x+7 between 3 and 4 correct to 3 decimal places by regula-falsi method. Then generalize the program for any equation whose real root lie between a and b. 
# Python Code :

# Defining Function
import math
def f(x):
    return 2*x-math.log10(x) - 7

# Implementing False Position Method
def falsePosition(x0,x1,e):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)


# python Output
First Guess: 3
Second Guess: 4
Tolerable Error: 0.00001


*** FALSE POSITION METHOD IMPLEMENTATION ***
Iteration-1, x2 = 3.787772 and f(x2) = -0.002839
Iteration-2, x2 = 3.789276 and f(x2) = -0.000005

Required root is: 3.78927580
