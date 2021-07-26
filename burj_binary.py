n = int(input())
l = len(str(bin(n))[2:])
for i in range(n+1):
    print(str(bin(i))[2:].rjust(l))
