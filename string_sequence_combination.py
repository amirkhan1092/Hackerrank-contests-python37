st,n = input().split()
n = int(n)

lt = []

for i in range(len(st)):
    for j in range(i,len(st)):
        d = st[i]+st[j]
        d = sorted(d)
        d = ''.join(d)
        lt.append(d)
lt.sort()

for kp in lt:
    print(kp)