n,k=map(int,input().split())
arr=[]
c=0
arr=list(map(int,input().split()))
for i in range(0,len(arr)-1):
    if i<k:
        c=c+arr[i]
print(c)
#tj
