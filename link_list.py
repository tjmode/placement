class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class sll:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.nextt
    def insert(self,data):
        nn=node(data)
        temp=self.head
        nn.nextt=temp
        self.head=nn

    def delete(self):
        temp=self.head
        self.head=temp.nextt
        temp.nextt=None

    def insertlast(self,f):
        temp=self.head
        while temp.nextt!=None:
            temp=temp.nextt
        nn=node(f)
        temp.nextt=nn

    def insertmed(self,med,ind):
        temp=self.head
        c=1
        while c<ind:
            temp=temp.nextt
            c+=1
        temp2=temp.nextt
        nn=node(med)
        temp.nextt=nn
        nn.nextt=temp2

    def deletelast(self):
        temp=self.head
        while temp.nextt.nextt!=None:
            temp=temp.nextt
        temp.nextt=None
            
        
        
        
        


obj=sll()
ch=0
while ch!=4:
    print("linked list\n 1.insert 2.delete 3.print 4.exit 5.insert at last 6.meed 7.last")
    ch=int(input())
    if ch==1:
        print("enter the value of to be insert ")
        data=input()
        obj.insert(data)
    elif ch==3:
        obj.printlist()
    elif ch==2:
        #delete=input()
        obj.delete()
    elif ch==4:
        break
    elif ch==5:
        f=input()
        obj.insertlast(f)
    elif ch==6:
        a=input()
        b=int(input())
        obj.insertmed(a,b)
    elif ch==7:
        obj.deletelast()
        
    else:
        print("vaipu ila raja")
