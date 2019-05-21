d=int(input())
s=list(map(int,input().split()))
c=0
for i in range(0,len(s)-1):
    for j in range(0,len(s)-1-i):
        if s[j]>s[j+1]:
            c=c+1
            s[j],s[j+1]=s[j+1],s[j]

print("Array is sorted in" +c+ "swaps")
print("First Element:"+min(s))
print("Last Element:"+max(s))
