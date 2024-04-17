import math
K=0.01;
L=3;
x=y=a=b=float();
x_values = [1, 2, 6.5]
print('Please enter value for X\n');
x=float(input());
a=0;
a=math.exp((1.0/5.0)*math.log (7.002 * math.sqrt(K) - 1 + 1/10 * (math.exp(x) + math.exp(-x))))
print('Result is A=',a,'\n');
b=0;
b=math.log10(L)*(math.cos(math.pi/5) + math.cos(3*math.pi/5))
print('Result is B=',b,'\n');
if a**2 + b**2 > 0.1:
    y= math.atan(5*a**2 + 7*b**2)
elif a**2 + b**2 <= 0.1:
    y=math.asin(5*a**2 + 7*b**2)
print('Result is Y=',y,'\n');
