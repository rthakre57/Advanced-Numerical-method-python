#Evaluate I=∫_0^1▒1/(1+x^2 ) dx correct to 3 decimal places by Trapezoidal and Simpson 1/3rd rule with h=0.5,0.25,0.125 respectively. 

# Trapezoidal Method
import math
# Define function to integrate
def f(x):
    return 1/(1 + x**2)
# calculating step size
#h = (xn - x0) / n
h=float(input('The value of h='))
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
n=0
n=((upper_limit-lower_limit)/h)
print("\nNumber of sub intervals: " , n)
sub_interval = int(input("\nNumber of sub intervals: "))

# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )

# Call Simpson's 1/3 () method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )   

#Python Output :
The value of h=0.5
Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals:  2.0

Number of sub intervals: 2
Integration result by Trapezoidal method is: 0.775000
Integration result by Simpson's 1/3 method is: 0.783333

The value of h=0.25
Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals:  4.0

Number of sub intervals: 4
Integration result by Trapezoidal method is: 0.782794
Integration result by Simpson's 1/3 method is: 0.785392

The value of h=0.125
Enter lower limit of integration: 0
Enter upper limit of integration: 1

Number of sub intervals:  8.0

Number of sub intervals: 8
Integration result by Trapezoidal method is: 0.784747
Integration result by Simpson's 1/3 method is: 0.785398
