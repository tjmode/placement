s=input()
a=[]
d=[]
c=[]
z=[]
for i in s:
    if i  not in a:
        a.append(i)
    else:
        d.append(i)
for i2 in a:
    if i2 not in d:
        z.append(i2)
print(*z)
