# Enter your code here. Read input from STDIN. Print output to STDOUT
# >>> from itertools import combinations_with_replacement
# >>>
# >>> print list(combinations_with_replacement('12345',2))
# [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,2))
# [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
# Sample Input
#
# HACK 2
# Sample Output
#
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

from itertools import combinations_with_replacement as cmbr
lt, r =input().split()
r = int(r)

hh = cmbr(lt,r)
result = []
for i in hh:
    s = sorted(i)
    tt = ''.join(s)
    result.append(tt)

result.sort()
for i in result:
    print(i)