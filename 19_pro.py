s=int(input())
n=[]
m=[]
y=[]
for i in range(s):
    f=list(map(int,input().split()))
    n.append(f)
for j in n:
    for q in j:
        m.append(q)

m.sort()

for t in m:
    if t==len(m):
        print(t,end="")
    else:
        print(t,end=" ")
