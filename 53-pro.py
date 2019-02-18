s=input()
a=[]
d=s.replace(" ","")
d1=d.lower()
for i in d1:
    if i not in a:
        a.append(i)
    
if len(a)==26:
    print("yes")
else:
    print("no")
