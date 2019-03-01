# Sample Input
# ['Hello world','online Data','Gla University']
# Sample Output
# [False, False, True]

a = eval(input())

res = []
for k in a:
    res.append(k.istitle())

print(res)