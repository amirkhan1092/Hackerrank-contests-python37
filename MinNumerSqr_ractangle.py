def MinSqr(r, c, k=0):
    if r > c:
        k += 1
        return MinSqr(r - c, c, k)
    elif r < c:
        k += 1
        return MinSqr(c - r, r, k)
    elif r == c:
        return k + 1


print(MinSqr(5, 2))
