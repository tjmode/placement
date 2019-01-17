s=int(input())
c=0
a=list(map(int,input().split()))
for i in range(a[0],a[1]):
    if i==s:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
