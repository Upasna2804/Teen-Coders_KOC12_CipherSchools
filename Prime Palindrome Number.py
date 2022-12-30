from math import sqrt
b=[]
c=[]
for k in range(2,10000000):
    m=k
    reversed_num=0
    while k!=0:
        digit = k % 10
        reversed_num = reversed_num * 10 + digit
        k//= 10
    if(m==reversed_num):
        b.append(m)
  
 
for i in b:
    t=0
    if(i>1):
        for j in range(2,int(sqrt(i))+1):
            if(i%j==0):
                t=1
                break
        if(t==0):
            c.append(i)
    
n=int(input("enter the number to find the nth prime palindrome:"))
print(c[n-1])