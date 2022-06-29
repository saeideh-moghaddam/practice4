import math
a=int(input("Please type the first number : "))
b=int(input("Please type the second number : "))
if (a>b):
    min1=a
else:
    min1=b
while (1):
    if(min1%a==0 and min1%b==0):
        print("k.m.m :",min1)
        break
    min1=min1+1    
