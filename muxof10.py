n = int(input())
if n<10:
    
    e=10-n
    e1=e+n
    print(e1)
else:
    a=[int(d) for d in str(n)]
    b=a[1]-10
    c=abs(b)
    n=n+c
    print(n)
