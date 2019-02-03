s=input()
t=0
o=0
for i in s:
    if i=="(":
        t=t+1
    elif i==")":
        o=o+1
if t==o:
    print("yes")
else:
    print("no")
