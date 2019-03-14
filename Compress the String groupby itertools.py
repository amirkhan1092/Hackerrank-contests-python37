
'''
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
'''


from itertools import groupby

nt = input()

root = groupby(nt)
kh = []
for i,k in root:
    ln = len(list(k))
    k = int(i[0])
    kh.append((ln,k))
for bp in kh:
    print(bp,end=' ')