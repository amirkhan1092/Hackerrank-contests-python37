# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

import itertools

a = eval(input('enter the list of numbers '))
k = eval(input('enter the number '))

flag = False

for i in range(1,len(a)):
        h = itertools.combinations(a,i)
        for m in h:
            if sum(m) == k:
                flag = True
                break

        if flag:
            break

print(flag)

#
# for i in range(len(a)):
#     for p in range(len(a)):
#         if a[i] + a[p] == k and i != p:
#             flag = True
#             break
#     if flag:
#         break
#
# print(flag)