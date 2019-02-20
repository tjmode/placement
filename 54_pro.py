x,y=map(int,input().split())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a=y1-y
b=y2-y3
c=x2-x1
d=x3-x
if a==b and c==d:
    print("yes")
else:
    print("no")
