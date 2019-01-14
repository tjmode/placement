s=input()
q=0
for i in s:
    if((i>='a' and i<='z') or (i>='A' and i<='Z')):
        q=q+1
print(q)
