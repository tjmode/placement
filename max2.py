number_array = list()
number = input()
for i in range(int(number)):
    n = input()
    number_array.append(int(n))
number_array.sort()
i=len(number_array)-1
print(number_array[i])
