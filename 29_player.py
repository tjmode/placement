t,y=map(int,input().split())
a=[]
q=[]
e=[]
for i in range(0,1000):
    s=i*i
    a.append(s)
for w in range (t,y+1):
    q.append(w)    
for r in a:
    if r in q:
        e.append(r)
print(len(e))
#ereh
