z=int(input())
s=list(map(int,input().split()))
d=[]
f=[]
g=[]
p=0
o=0
for i in s:
    d.append(i)
    f.append(i)
f.sort()
for i in d:
    p=p+1
    if i==f[0]:
        g.append(p)

for j in d:
    o=o+1
    if j==f[len(f)-1]:
        g.append(o)
print(g[0],g[1])
