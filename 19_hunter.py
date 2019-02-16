s,s1=map(int,input().split())
f=0
q=[]
q1=[]
q2=[]
q3=[]
for i in range(0,s):
    w=list(map(int,input().split()))
    q.append(w)
for j in q:
    for k in j:
        q1.append(k)
for k1 in q1:
    if k1 not in q2:
        q2.append(k1)
    else:
        q3.append(k1)
w1=set(q3)
for z in w1:
    f=f+1
    if f==len(w1):
        print(z,end="")
    else:
        print(z,end=" ")
