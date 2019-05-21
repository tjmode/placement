class stack:
    
    def __init__(self):
        
        
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    def print(self):
        return s.items

s=stack()
while True:
    print("push value")
    print("pop")
    print("quit")
    print("print")
    do=input("what need to do ").split()

    op=do[0].strip().lower()
    if op=="push":
        s.push(int(do[1]))
    elif op=="pop":
        if s.is_empty():
            print("number enga da")
        else:
            print("popped value:",s.pop())
            print(s.items)
    elif op=="print":
        s.print()
        print(s.items)
    elif operation == 'quit':
        break
