s=int(input())
n=[]
m=[]
y=[]
s1=0
for i in range(s):
    f=list(map(int,input().split()))
    n.append(f)
for j in n:
    for q in j:
        m.append(q)

m.sort()
print(len(m))
for t in m:
    s1=s1+1
    if (s1==len(m)):
        print(t,end="")
    else:
        print(t,end=" ")
