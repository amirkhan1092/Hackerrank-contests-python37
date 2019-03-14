def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
             return False
    return True

print(is_arithmetic([5, 7, 9, 11]))
print(is_arithmetic([5, 8, 9, 11]))