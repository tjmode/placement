i=int(input())
s=input()
v=("a","e","i","o","u","U","O","I","E","A")
for x in s.lower():
    
    if x in v:
       s=s.replace(x,"")
print(s[::-1])
