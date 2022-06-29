import math
a = int(input("enter your number1:"))
b= int(input("enter yore number2:"))

def mult(a , b):
    for i in range(1 , a+1):
        for j in range(1,b+1):
            print('{:>4}'.format(i*j),end='')
            if j == b :
                print()
mult(a , b)