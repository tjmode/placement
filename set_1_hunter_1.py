a1=int(input())
f=input()
s=f.replace(" ", "")
a=[]
d=[]
for i in s:
    if i not in a:
        a.append(i)
    else:
        d.append(i)
m="".join(set(d))
o=sorted(m)
g=0
for y in o:
    if g==len(o)-1:
        print(y,end="")
    else:
        g=g+1
        print(y,end=" ")
