s=[1,2,3,4,5]
arr=[[]]
arr3=[]
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        arr.append(sub)
for j in arr:
    r=1
    for k in j:
        r=r*k
    arr3.append(r)
print(max(arr3))
