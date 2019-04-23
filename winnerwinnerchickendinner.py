# ravi,shastri,raman,ravi,shalini,shalini
a = input().strip().split(',')
d = {}
for i in a:
    d[i] = a.count(i)

mx = max(d.values())
h = []
for i in d:
    if d[i] == mx:
        h.append(i)

h.sort(key = len)
print('Winner ',h[0])


