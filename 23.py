n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
for i in range(0,len(b)):
    if(i==len(b)-1):
        print(b[i],end="")
    else:
        print(b[i],end=" ")
