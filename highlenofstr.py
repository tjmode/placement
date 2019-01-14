s=input()
a=s.split()
if len(a[0])==len(a[1]):
    print(a[1])
elif len(a[0])<len(a[1]):
    print(a[1])
else:
    print(a[0])
