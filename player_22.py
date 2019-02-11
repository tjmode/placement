s,w=map(int,input().split())
a=[]
for i in range(1,w+1):
    if s%i==0 and w%i==0:
        a.append(i)
print(max(a))
