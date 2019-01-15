s=int(input())
n=0
c=0
while s>n:
    a=s%10
    c=a+c
   
    s=s//10
print(c)
