a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
s=0
for i in b:
    if i==a[1]:
        c=c+1
    else:
        s=s+1

if c>=1:
    print("yes")
else:
    print("no")
