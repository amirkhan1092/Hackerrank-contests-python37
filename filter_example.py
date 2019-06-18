def fit(s):
    if s%2 == 0:
        return True
    else:
        return False

a = [1,2,3,4,5,5,6,8,9]

res = filter(fit,a)
print(list(res))
