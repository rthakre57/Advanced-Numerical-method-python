#(RTMNU Practical Problem 2 )Find a real root of a cubic equation using Newton-Raphson method, correct to four decimal places. 

# Python Code:
# Defining Function
def f(x):
    return x**3 - 5*x - 9

# Defining derivative of function
def g(x):
    return 3*x**2 - 5

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


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
newtonRaphson(x0,e,N)

#Python Output :
Enter Guess: 2
Tolerable Error: 0.00001
Maximum Step: 10


*** NEWTON RAPHSON METHOD IMPLEMENTATION ***
Iteration-1, x1 = 3.571429 and f(x1) = 18.696793
Iteration-2, x1 = 3.009378 and f(x1) = 3.207103
Iteration-3, x1 = 2.864712 and f(x1) = 0.185915
Iteration-4, x1 = 2.855236 and f(x1) = 0.000771
Iteration-5, x1 = 2.855197 and f(x1) = 0.000000

Required root is: 2.85519654
