n = int(input('enter the number of rows '))
for row in range(n):
    print(' '*(n-row-1),end='')
    p=1
    for col in range(row+1):
        print(p,end=' ')
        p=int(p*(row-col)/(col+1))
    print()
