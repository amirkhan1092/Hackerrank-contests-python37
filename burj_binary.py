n = int(input('enter the number '))
h = len(str(bin(n))[2:])

for k in range(n+1):
    tt=str(bin(k))[2:]
    p=len(tt)
    print(' '*(h-p)+tt)

