s,w=map(int,input().split())
q=[]
for i in range(1,10000000000000000000000000000000):
    if i%s==0 and i%w==0:
        print(i)
        break
