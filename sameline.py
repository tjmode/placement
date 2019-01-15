x=int(input())
n=0
b=(str(x)[::-1])
a=int(b)
while a>n:
    s=a%10
    print(s,end=" ")
    a=a//10
