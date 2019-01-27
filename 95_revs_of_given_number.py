n=int(input())
s=0
while n>0:
    e=n%10
    s=s*10+e
    n=n//10
print(s)
