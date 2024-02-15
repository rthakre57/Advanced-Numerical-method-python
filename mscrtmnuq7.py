#Find the smallest root of the equation x^3-9x^2+26x-24=0, by Ramanujan’s method, generalize the program. 

#python Code:

import numpy as np
n = int(input('Enter degree of polynomial equation: '))
c = np.zeros((n+1))
a = np.zeros((n+1))
for i in range(n+1):
	c[i]=int(input('Coefficient of x^'+str(i)+'='))

for i in range(1,n+1):
	a[i]=-c[i]/c[0]
	print('Value of a'+str(i)+'=',a[i])


#to find b
m = int(input('Maximum iteration for Ramanuja method: '))
d = np.zeros((m+1))
for i in range(m+1):
	if i>n:
		d[i]=0
	else:
		d[i]=a[i]

b=np.zeros((m+1))
b[1]=1
for i in range(2,m):
	for j in range(1,i):
		b[i]+=d[j]*b[i-j]

	
	print('Value of b'+str(i)+'=',b[i])

for i in range(2,m):
	print('b'+str(i-1)+'/ b'+str(i)+'=', b[i-1]/b[i])
	if (round(b[i-2]/b[i-1],2)==round(b[i-1]/b[i],2)):
		print('By Ramanujan method Succesive convergent approach the value : %0.5f' %round(b[i-1]/b[i]))
		break

#python Output :
Enter degree of polynomial equation: 3
Coefficient of x^0=-24
Coefficient of x^1=26
Coefficient of x^2=-9
Coefficient of x^3=1
Value of a1= 1.0833333333333333
Value of a2= -0.375
Value of a3= 0.041666666666666664
Maximum iteration for Ramanuja method: 15
Value of b2= 1.0833333333333333
Value of b3= 0.7986111111111109
Value of b4= 0.5005787037037034
Value of b5= 0.2879533179012342
Value of b6= 0.15750787680041117
Value of b7= 0.0835084849751369
Value of b8= 0.043400126502128863
Value of b9= 0.022263950044980396
Value of b10= 0.011323751984394476
Value of b11= 0.005726755320481737
Value of b12= 0.002885242521581469
Value of b13= 0.0014499691525490434
Value of b14= 0.0007274487746884851
b1/ b2= 0.9230769230769231
b2/ b3= 1.356521739130435
b3/ b4= 1.5953757225433534
b4/ b5= 1.7384022776754324
b5/ b6= 1.8281836042150401
b6/ b7= 1.8861302159571716
b7/ b8= 1.9241530314673307
b8/ b9= 1.9493453055026866
b9/ b10= 1.9661283712026596
b10/ b11= 1.9773416796584768
b11/ b12= 1.9848436579060147
By Ramanujan method Succesive convergent approach the value : 2.00000
