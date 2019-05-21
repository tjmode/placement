inp=int(input())
f=[]
for i in range(0,inp):
    first=input()
    second=input()
    s=list(set(first)&set(second))
    if len(s)>=1:
        f.append("YES")
    else:
        f.append("NO")
for j in f:
    print(j)
