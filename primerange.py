f,s= [int(x) for x in input().split()]  
for num in range(f,s+1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num,end=" ")
           #tont
