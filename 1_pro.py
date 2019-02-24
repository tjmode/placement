import os
s=int(input())
d=[]
for i in range(0,s):
    i=input()
    d.append(i)
print(os.path.commonprefix(d))
