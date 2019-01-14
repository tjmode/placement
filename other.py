s=input()
numbers = sum(c.isdigit() for c in s)
words   = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)
others  = len(s) - numbers - words - spaces
print(others)
