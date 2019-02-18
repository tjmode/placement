w,e=map(int,input().split())
s=list(map(int,input().split()))
d=list(map(int,input().split()))
c=0
for i in s:
    if i in d:
        c=c+1
if c==len(d):
    print("YES")
else:
    print("NO")
