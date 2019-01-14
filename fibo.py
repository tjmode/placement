s=int(input())
a=0
b=1
n=0
while n<s:
    c=a+b
    a=b
    b=c
    n=n+1
    if n==s:
        print(c)
    else:
        print(c,end=" ")
