q1=int(input())
s=list(map(int,input().split()))
a=[]
for i in s:
    a.append(i)
a.sort()
if s==a:
    print("yes")
else:
    print("no")
