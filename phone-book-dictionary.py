a = int(input())
k = []
for i in range(a):
    k.append(input().split())

l = []
for p in range(a):
    l.append(input())

k = dict(k)
for i in l:
    if i in k:
        print('{}={}'.format(i, k[i]))
    else:
        print('Not found')