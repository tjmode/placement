p=0
a=0
q=0
w=0
e=0
s=input()
d=s.split('@')
d2=d[1].split(".")
if len(d[0])>=3 :
       p=p+1
if (len(d2[0])==4)or (len(d2[2])==5):
    a=a+1
if d2[1]=="com":
    e=e+1
for i in s:
    if i=="@":
        q=q+1
    elif i==".":
        w=w+1
if (p==1 and a==1 and q==1 and w==1 and e==1):
    print("YES")
else:
    print("NO")
