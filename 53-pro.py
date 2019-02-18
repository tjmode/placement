s=input()
a=[]
j1=0
d=s.replace(" ","")
d1=d.lower()
for i in d1:
    if i not in a:
        a.append(i)
for j in a:
    j1=j1+1
if j1==26:
    print("yes")
else:
    print("no")
