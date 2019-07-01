def even_odd(n):
    ise = 'Even'
    for i in range(1, n+1):
        ise = 'Odd' if ise == 'Even' else 'Even'
    return ise


a = int(input('enter the number '))
res = even_odd(a)
print(res)
