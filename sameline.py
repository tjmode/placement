x=int(input())
n=0
b=(str(x)[::-1])
c=len(b)
a=int(b)
while a>n:
    s=a%10
    n=n+1
    if n==c:
        print(s,end="")
    else:
        print(s,end=" ")
    a=a//10
