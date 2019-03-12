
# https://www.hackerrank.com/contests/python37-l7/challenges/the-ship-teams

d = eval(input())
t1 = []
t2 = []
for i in d:
    if d[i] < 20 or d[i] > 40:
        t1.append(i)
    elif d[i] > 20 or d[i]<40:
        t2.append(i)

t1.sort()
t2.sort()

print('[')
print(' ',t1,',',sep='')
print('',t2)
print(']')