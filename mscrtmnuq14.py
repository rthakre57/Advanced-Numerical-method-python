Q.14 Match ∫ √(approx.) by Trapezoidal and Simpsons rules (both) with number of subintervals 10, 20, 30, 40, 50

# Trapezoidal Method
import math
# Define function to integrate
def f(x):
    return math.sqrt(1-x**2)

# Implementing trapezoidal method
def trapezoidal(x0,xn,n):
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration

def simpson13(x0,xn,n):
    
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    
    # Finding final integration value
    integration = integration * h/3
    
    return integration
    

# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("\nNumber of sub intervals: "))

#Calculate step size h
h=0
h=((upper_limit-lower_limit)/sub_interval)
print("\nstep size: " , h)


# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )

# Call Simpson's 1/3 () method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )   

Python Output:
Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals: 10

step size:  0.1
Integration result by Trapezoidal method is: 0.776130
Integration result by Simpson's 1/3 method is: 0.781752


Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals: 20

step size:  0.05
Integration result by Trapezoidal method is: 0.782116
Integration result by Simpson's 1/3 method is: 0.784112


Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals: 30

step size:  0.03333333333333333
Integration result by Trapezoidal method is: 0.783611
Integration result by Simpson's 1/3 method is: 0.784698


Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals: 40

step size:  0.025
Integration result by Trapezoidal method is: 0.784237
Integration result by Simpson's 1/3 method is: 0.784944


Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals: 50

step size:  0.02
Integration result by Trapezoidal method is: 0.784567
Integration result by Simpson's 1/3 method is: 0.785073
