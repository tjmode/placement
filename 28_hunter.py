s=input()
d=[]
c=""
for i in s:
    if i not in d:
        d.append(i)
        c=c+i
print(c)
