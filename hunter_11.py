n=input()
a=[]
for n1 in n.split():
	temp=n1[::-1]
	a.append(temp)
print(*a)
