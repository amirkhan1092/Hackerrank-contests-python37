#https://www.hackerrank.com/contests/python-lab-04/challenges/color-combinations

l = eval(input())
c = {'R','B','G'}
while len(l) != 1:
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            s = [l[i],l[i+1]]
            r = [j for j in c if j not in s]
            l.remove(l[i])
            l.remove(l[i])
            l.insert(i,r[0])
            break
print('"{}"'.format(l[0]))
