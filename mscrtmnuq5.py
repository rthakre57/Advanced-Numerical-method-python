#	Evaluate √N by applying Newton’s formula correct to three decimal places. Generalize the program. 

# Implementing Newton Raphson Method

# python Code :

def newtonRaphson(x0,e,M,N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if  x0 == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = (1/2)*(x0 + N/x0)
        print('Iteration-%d, x1 = %0.6f ' % (step, x1))
        x0 = x1
        step = step + 1
        
        if step > M:
            flag = 0
            break
        
        condition = abs(N-x1**2) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
N = int(input('Evaluate √N : Enter the number N :'))
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
M = input('Maximum Step: ')


# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
M = int(M)

# Starting Newton Raphson Method
newtonRaphson(x0,e,M,N)

#python Output:
Evaluate √N : Enter the number N :12
Enter Guess: 3
Tolerable Error: 0.00001
Maximum Step: 15


*** NEWTON RAPHSON METHOD IMPLEMENTATION ***
Iteration-1, x1 = 3.500000
Iteration-2, x1 = 3.464286
Iteration-3, x1 = 3.464102

Required root is: 3.46410162
