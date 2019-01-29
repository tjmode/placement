r=int(input())
p=list(map(int,input().split()))
y=sorted(p,reverse=True)
if y==[0,0,0,0,0]:
    print(0)
else:
    for i in y:
        print(i,end="")
