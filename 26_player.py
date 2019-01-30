a=input()
c=0
d=0
for i in a:
    if i.isnumeric():
        c=c+1
    else:
        d=d+1
if d<1:
    print("yes")
else:
    print("no")
