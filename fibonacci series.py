
def fib(n):
    if n <= 1:
        return n
    else:

        return fib(n-1) + fib(n-2)

# print(fib(0))


num = int(input('enter the length of fibonacci series '))
for i in range(num):
    f = fib(i)
    print(f)








#
#
# num = int(input('enter the length of fibonacci series '))
#
# a = 0
# b = 1
# lst = []
# lst.extend((a,b))
# for i in range(num-2):
#     temp = a + b
#     lst.append(temp)
#     a = b
#     b = temp
#
# print(lst)

