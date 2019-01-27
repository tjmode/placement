s=input()
d=s.split()
a=list(d[0])
b=list(d[1])
f=0
q=0
for i in a:
    for j in b:
        if i==j:
            f=f+1
        else:
            
            q=q+1
if q<=2:
    print("yes")
else:
    print("no")
