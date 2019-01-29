e=int(input())
s=input()
a=[]
x=[]
d=s.replace(" ","")
for i in d:
    if i not in a:
        a.append(i)
        
    else:
        x.append(i)
w=[]
for z in a:
    if z not in x:
        print(z,end="")
