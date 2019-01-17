a=int(input())
c=0
b=[int(d) for d in str(a)]
for i in b:
    if i>=2:
        c=c+1
    else:
        d=0
if c<1:
    print("yes")
else:
    print("no")
