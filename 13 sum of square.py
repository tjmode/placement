a=int(input())
s=0
while a>0:
    b=a%10
    z=b*b
    s=s+z
    a=a//10
print(s)
