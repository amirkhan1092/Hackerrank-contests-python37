a = int(input('enter the number of line '))

for i in range(a):
    try:
        n, r = map(int,input().split())
        print(n/r)
    except Exception as e:
        print(e)




