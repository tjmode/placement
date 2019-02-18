d=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(0,len(a)):
    if a[i]==i:
        b.append(a[i])
b.sort()
for i1 in b:
    if c==len(b)-1:
        print(i1,end="")
    else:
        print(i1,end=' ')
