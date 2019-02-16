e=input()
b=0
j1=0
a=[]
a1=[]
s=list(map(int,input().split()))
s1=len(s)/2
w=s1+0.1
w1=round(w)
for i in s:
    
    b=b+1
    if b<=w1:
        a.append(i)
    else:
        a1.append(i)
a2=a1+a
for j in a2:
    j1=j1+1
    if j1==len(a2):
        print(j,end="")
    else:
        print(j,end=' ')
