
# 23dsa43dsa98
# 98 output
a = input('enter the string having number s ')

z = ' '
for i in a:
    if i.isalpha():
        z += " "
    else:
        z +=i
x = z.split()
x = [int(i) for i in x]
print(max(x))
