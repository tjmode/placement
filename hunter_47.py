import re
s=input()
d=re.sub('\s{2,}', ' ', s)
print(d.strip())
#tony_wilson
