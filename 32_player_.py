a,b=map(int,input().split())
s=list(map(int,input().split()))
f=0
l=0
for i in s:
    if i == b:
        f=f+1
    else:
        l=l+1

if f==1:
    print("Yes")
else:
    print("No")
