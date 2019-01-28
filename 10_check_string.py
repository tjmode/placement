x=input()
s=x.split()
a=s[0]
b=s[1]
c=[i for i in range(len(a)) if a[i] != b[i]]
if len(c)<=1:
    print("yes")
else:
    print("no")
