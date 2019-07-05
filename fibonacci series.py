
num = int(input('enter the length of fibonacci series '))

a = 0
b = 1
lst = []
lst.extend((a,b))
for i in range(num-2):
    temp = a + b
    lst.append(temp)
    a = b
    b = temp

print(lst)

