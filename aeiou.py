f=input()
s=0
c=0
for i in f:
    
    if i in ('a', 'e', 'i', 'o', 'u'):
        c=c+1
if c>0:
    print("yes")
else:
    print("no")
