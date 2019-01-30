e=int(input())
a=list(map(int,input().split()))
t=[]
d=[]
for i in a:
    if i not in t:
        t.append(i)
    else:
        d.append(i)
h=[]
x=[]
for r in t:
    if r not in d:
        x.append(r)
        
    else:
        h.append(r)
print(x[0])
