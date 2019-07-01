k = int(input('enter the number '))
qw = int(input('enter the number of questions '))

qlirank = []
for i in range(qw):
    qlirank.append(int(input()))


va = 1
va1 = qlirank[0]
for p in range(1, len(qlirank),2):

    if (qlirank[p-1] - va1) >= k or (qlirank[p] - va1) >= k:
        break
    va += 1

print(va)


