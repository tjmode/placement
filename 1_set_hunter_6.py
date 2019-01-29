y=int(input())
s=input()
f=s.replace(" ","")
t=[]
o=[]
for n in f:
    if n not in t:
        t.append(n)
    else:
        o.append(n)
        
if o==[]:
    print("unique")
else:
    print(o[0])
