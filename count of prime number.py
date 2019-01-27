n,m=map(int,input().split())
arr=[]
for i in range(n,m+1):
    if i>1:
        for s in range(2,i):
            if(i%s)==0:
                break
        else:
            arr.append(i)
print(len(arr))
