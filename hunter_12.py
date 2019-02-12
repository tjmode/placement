d,m=map(int,input().split())
s=list(map(int,input().split()))
q=sorted(s, reverse=True)
print(q[m-1])
