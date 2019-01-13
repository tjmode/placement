n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
for i in range(0,len(a)):
    if(i==len(a)):
        print(b[i],end="")
    else:
        print(b[i],end=" ")
