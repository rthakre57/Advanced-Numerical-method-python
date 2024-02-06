# 	Find a double root of the equation x^3-x^2-x+1=0 by generalized Newton’s formula.
#Python code :
# Defining Function
def f(x):
    return x**3 - x**2 - x+1

# Defining derivative of function
def g(x):
    return 3*x**2 - 2*x-1

def h(x):
    return 6*x-2

# Implementing Newton Raphson Method
def GennewtonRaphson1(x0,e,N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step1 = 1
    flag1 = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1=x0-2*f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step1, x1, f(x1)))
        x0 = x1
        step1 = step1 + 1
        
        if step1 > N:
            flag1 = 0
            break
        
        condition = abs(f(x1)) > e

    
    if flag1==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

    
def x1(x0,e,N):
    step1 = 1
    flag1 = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            break
        x1=x0-2*f(x0)/g(x0)
        x0 = x1
        step1 = step1 + 1
        
        if step1 > N:
            flag1 = 0
            break
        
        condition = abs(f(x1)) > e
    return x1

def GennewtonRaphson2(x0,e,N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step2=1
    flag2=1
    condition = True
    while condition:
        if h(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x2 = x0 - (2-1)*g(x0)/h(x0)
        
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step2, x2, f(x2)))
        x0 = x2
        step2 = step2 + 1
        
        if step2 > N:
            flag2 = 0
            break
        
        condition = abs(f(x2)) > e
    
    if flag2==1:
        print('\nRequired root is: %0.8f' % x2)
    else:
        print('\nNot Convergent.')

    
def x2(x0,e,N):
    step2=1
    flag2=1
    condition = True
    while condition:
        if h(x0) == 0.0:
            break
        
        x2 = x0 - (2-1)*g(x0)/h(x0)
        x0 = x2
        step2 = step2 + 1
        
        if step2 > N:
            flag2 = 0
            break
        
        condition = abs(f(x2)) > e
    return x2

# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
GennewtonRaphson1(x0,e,N)
GennewtonRaphson2(x0,e,N)
if(round(x1(x0,e,N),2)==round(x2(x0,e,N),2)):
    print('\n We Conclude that there double root at x0=%0.6f it is sufficiently close to actual root x1=%d' %(x2(x0,e,N),int(x1(x0,e,N))))

# Python Output1 :
Enter Guess: 0.8
Tolerable Error: 0.000001
Maximum Step: 15


*** NEWTON RAPHSON METHOD IMPLEMENTATION ***
Iteration-1, x1 = 1.011765 and f(x1) = 0.000278
Iteration-2, x1 = 1.000034 and f(x1) = 0.000000

Required root is: 1.00003430


*** NEWTON RAPHSON METHOD IMPLEMENTATION ***
Iteration-1, x2 = 1.042857 and f(x2) = 0.003752
Iteration-2, x2 = 1.001294 and f(x2) = 0.000003
Iteration-3, x2 = 1.000001 and f(x2) = 0.000000

Required root is: 1.00000125

 We Conclude that there double root at x0=1.000001 it is sufficiently close to actual root x1=1

#Python Output2:
Enter Guess: 1.1
Tolerable Error: 0.000001
Maximum Step: 15


*** NEWTON RAPHSON METHOD IMPLEMENTATION ***
Iteration-1, x1 = 1.002326 and f(x1) = 0.000011
Iteration-2, x1 = 1.000001 and f(x1) = 0.000000

Required root is: 1.00000135


*** NEWTON RAPHSON METHOD IMPLEMENTATION ***
Iteration-1, x2 = 1.006522 and f(x2) = 0.000085
Iteration-2, x2 = 1.000032 and f(x2) = 0.000000

Required root is: 1.00003159

 We Conclude that there double root at x0=1.000032 it is sufficiently close to actual root x1=1
