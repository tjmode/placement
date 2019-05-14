def print_formatted(number):
    # your code goes here
   for i in range(n):
        i=i+1
        d=i
        f=oct(i)
        g=bin(i)
        h=hex(i)
        f1=str(f)
        g1=str(g)
        h1=str(h)
        print(i,"",f1[2:len(f1)+1],"",h1[2:len(h1)+1],"",g1[2:len(g1)+10])
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
